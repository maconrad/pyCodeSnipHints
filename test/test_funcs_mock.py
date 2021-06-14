from unittest import mock

import pytest

from snips import get_ip
from snips import guess_number
from snips import hello
from snips import randum_sum

# Problem without Mocking: Return value of random is not always the same -> Mock
# Important: roll_dice from pypi2_testing call should be replaced with a mock object
#  Not the roll_dice function from the other package. Remember replace locally!
# Mock objects can have return values configured / mocked
# mock.patch under the hood creates a mock.Mock() object
#  and this is automatically injected into the testing function as a parameter
#  but this could be manually created like:
#  roll_dice = mock.Mock(name='roll dice mock', return_value=3)

@pytest.mark.parametrize("_input, expected", [(3, "You won!"), (4, "You lost!")])
@mock.patch("snips.pypi2_testing.roll_dice")
def test_guess_number(mock_roll_dice, _input, expected):
    mock_roll_dice.return_value = 3
    assert guess_number(_input) == expected
    mock_roll_dice.assert_called_once()

# Problem without Mocking: Dependency on API, maybe down, no network connectivity etc.
# 2 Options:
# 1st Option
#  mock_response = mock.Mock()
#  mock_response.json.return_value = {"origin": "0.0.0.0"}
#  mock_response.status_code = 200
# 2nd Option / shortcut:
#  mock_response = mock.Mock(return_value=2, status_code=200) -> works
#  mock_response = mock.Mock(json.return_value=...) -> NOT OK
#  --> Need dictionary unpacking to solve it
#  mock_response = mock.Mock(name='mock response', **{"status_code": 200, "json.return_value": {"origin": "0.0.0.0"}})

@mock.patch("snips.pypi2_testing.requests.get")
def test_get_ip(mock_requests_get):
    # 1st Mock returns another Mock object
    #  Request Get Mock returns a Response Mock
    mock_requests_get.return_value = mock.Mock(
        name='mock response', **{
            "status_code": 200,
            "json.return_value": {"origin": "0.0.0.0"}
        }
    )
    assert get_ip() == '0.0.0.0'

    # Can verify that mock was called with the following arguments
    mock_requests_get.assert_called_with("https://httpbin.org/ip")

# Side Effects
# If mock called 1st time return x, 2nd time y, 3rd time z
# Throws stop iteration
# Side effects can achieve predictability
# Side effects can throw Exceptions
# Side effect can also reference a function

@mock.patch("snips.pypi2_testing.random.randint")
def test_randum_sum(mock_randint):
    mock_randint.side_effect = [3, 4]
    assert randum_sum() == 7


# Multiple many dependencies in a single unit test
# Stack @mock.patch -> order important

@mock.patch("snips.pypi2_testing.random.randint")
@mock.patch("snips.pypi2_testing.time.time")
@mock.patch("snips.pypi2_testing.requests.get")
def test_silly(mock_requests_get, mock_time, mock_randint):
    assert hello() == 'hello'

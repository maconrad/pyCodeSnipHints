import sys

import pytest

from snips import funcs_testing

# @pytest.fixture(scope='function') is the default
@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

def test_format_data_for_display(example_people_data):
    assert funcs_testing.format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

# Pytest looks in conftest.py for fixtures as well
def test_format_data_for_display2(example_people_data2):
    assert funcs_testing.format_data_for_display(example_people_data2) == [
        "Alfoneeeee Ruiz: Senior Software Engineer",
        "Sayideeee Khan: Project Manager",
    ]

@pytest.mark.dummy
def test_hello():
    assert funcs_testing.hello() == 'hello'

@pytest.mark.dummy
def test_hello3():
    assert funcs_testing.hello() == 'hello'

@pytest.mark.skipif(sys.version_info > (3, 7), reason='Skipping for greater 3.7')
def test_add_num():
    assert (1 + 2) == 3

@pytest.mark.xfail(sys.platform == "darwin", reason='Failing on OSX darwin okey')
def test_add_xy():
    # dummy exception here
    # xfail used e.g. test on linux and windows but
    # we know that test will fail on windows
    # -> Skipped, not whole tests fail
    assert (1 + 2) == 3
    raise Exception()

@pytest.mark.parametrize("integer_list, below_value, expected_result", [
    ([1, 2, 3, 4], 10, True),
    ([1, 2, 2, 4], 10, True),
    ([1, 2, 2, 5], 10, True),
    ([1, 2, 2, 6, 3], 10, False),
])
def test_below(integer_list, below_value, expected_result):
    assert funcs_testing.below2(integer_list=integer_list, below_value=below_value) == expected_result

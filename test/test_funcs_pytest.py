import pytest

from snips import funcs_testing

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

@pytest.mark.dummy
def test_hello():
    assert funcs_testing.hello() == 'hello'

@pytest.mark.parametrize("integer_list, below_value, expected_result", [
    ([1, 2, 3, 4], 10, True),
    ([1, 2, 2, 4], 10, True),
    ([1, 2, 2, 5], 10, True),
    ([1, 2, 2, 6, 3], 10, False),
])
def test_below(integer_list, below_value, expected_result):
    assert funcs_testing.below2(integer_list=integer_list, below_value=below_value) == expected_result

# pytest looks for fixtures in this file
import pytest

@pytest.fixture
def example_people_data2():
    return [
        {
            "given_name": "Alfoneeeee",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayideeee",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]

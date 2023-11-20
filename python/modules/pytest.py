import pytest
import requests


# test assert examples

def test_uppercase():
    assert 'loud noises'.upper() == 'LOUD NOISES'

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_always_passes():
    assert True

def test_always_fails():
    assert False




# fixture demo

@pytest.fixture
def example_fixture():
    return 1

def test_with_fixture(example_fixture):
    assert example_fixture == 1




"""WHEN TO USE FIXTURES"""

# (TDD = test driven development)


# The data represents a list of people, each with a given name, family name, and job title. The function should output a list of strings that include each person’s full name (their given_name followed by their family_name), a colon, and their title:


# format_data.py

def format_data_for_display(peope):
    ... # implement this

def format_data_for_excel(people):
    ... # implement this


# test_format_data.py

def test_format_data_for_display():
    people = [
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

    assert format_data_for_display(people) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def test_format_data_for_excel():
    people = [
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

    assert format_data_for_excel(people) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""


         # now with fixture


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
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""



"""CONFTEST"""


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError('Network access not allowed during testing')
    monkeypatch.setattr(requests, 'get', lambda *args, **kwargs: stunted_get())

# By placing disable_network_calls() in conftest.py and adding the autouse=True option, you ensure that network calls will be disabled in every test across the suite. Any test that executes code calling requests.get() will raise a RuntimeError indicating that an unexpected network call would have occurred.

# MONKEYPATCH/MOCK modules ????????????



"""Parametrazation: Combining Tests/MARKS"""


def is_palindrome(text1):
    for i in range(len(text1)):
        if i >= len(text1[- 1 - i]):
            break 
        if text1[i] != text1[- 1 - i]:
            return False
    return True


def test_is_palindrome_empty_string():
    assert is_palindrome("")

def test_is_palindrome_single_character():
    assert is_palindrome("a")

def test_is_palindrome_mixed_casing():
    assert is_palindrome("Bob")

def test_is_palindrome_with_spaces():
    assert is_palindrome("Never odd or even")

def test_is_palindrome_with_punctuation():
    assert is_palindrome("Do geese see God?")

###

def test_is_palindrome_not_palindrome():
    assert not is_palindrome("abc")

def test_is_palindrome_not_quite():
    assert not is_palindrome("abab")


# SAME SHAPE
# def test_is_palindrome_<in some situation>():
#     assert is_palindrome("<some string>")


# so lets make MARKS:

@pytest.mark.parametrize('palindrome', [
    '',
    'a',
    'Bob',
    'Never odd or even',
    'Do geese see God?'
])

def test_is_palindrome(palindrome):
    assert is_palindrome(palindrome)


@pytest.mark.parametrize('non_palindrome', [
    'abc',
    'abab'
])

def test_is_palindrome_not_palindrome(non_palindrome):
    assert not is_palindrome(non_palindrome)


# combine all to one (НУЖНО ЛИ ???)

@pytest.mark.parametrize('maybe_palindrome, expected_result', [
    ('', True),
    ('a', True),
    ('Bob', True),
    ('Never odd or even', True),
    ('Do geese see God?', True),
    ('abc', False),
    ('abab', False),
])
def test_is_palindrome(maybe_palindrome, expected_result):
    assert is_palindrome(maybe_palindrome) == expected_result


# some theory
# overhead is any combination of excess or indirect computation time, memory, bandwidth, or other resources that are required to perform a specific task


# --durations expects an integer value n and will report the slowest n number of tests.
# -vv to show hidden and more info



"""USEFUL PLUGINS"""

# pytest -randomly

# Often the order of your tests is unimportant, but as your codebase grows, you may inadvertently introduce some side effects that could cause some tests to fail if they were run out of order.


# pytest-cov

# If you want to measure how well your tests cover your implementation code, then you can use the coverage package. pytest-cov integrates coverage, so you can run pytest --cov to see the test coverage report and boast about it on your project front page.


# pytest-django

# pytest-django provides a handful of useful fixtures and marks for dealing with Django tests. You saw the django_db mark earlier in this tutorial. The rf fixture provides direct access to an instance of Django’s RequestFactory. The settings fixture provides a quick way to set or override Django settings. These plugins are a great boost to your Django testing productivity!


# pytest-bdd

# pytest can be used to run tests that fall outside the traditional scope of unit testing. Behavior-driven development (BDD) encourages writing plain-language descriptions of likely user actions and expectations, which you can then use to determine whether to implement a given feature. pytest-bdd helps you use Gherkin to write feature tests for your code.
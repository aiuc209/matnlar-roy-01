import pytest
import re

def remove_emoji_and_special_chars(text):
    return re.sub(r'[^\w\s]', '', text)

@pytest.mark.parametrize("text, expected", [
    ("Hello, world! 🌎", "Hello world"),
    ("This is a test @#$%", "This is a test"),
    ("Foo bar baz 😊", "Foo bar baz"),
    ("Qux quux quuz 👍", "Qux quux quuz"),
])
def test_remove_emoji_and_special_chars(text, expected):
    assert remove_emoji_and_special_chars(text) == expected

from app import index

def test_index():
    assert index() == "Hello, world!"

def test_home():
    assert home() == "Hello, home!"

def test_profile():
    assert profile() == "It's your profile!"

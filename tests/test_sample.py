from buggy_code import get_user_name

def test_get_user_name():
    assert get_user_name({}) == "Guest"

from userManager import UserManager
import pytest

@pytest.fixture
def user_manager():
    "Creates a fresh instance of UserManager before each test"
    return UserManager()

def test_add_user(user_manager):
    assert user_manager.add_users("john_doe","john@example.com") == True
    assert user_manager.add_users("smith", "smith@example.com") == True

def test_duplicate_add_user(user_manager):
    user_manager.add_users("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_users("john_doe", "random@example.com")
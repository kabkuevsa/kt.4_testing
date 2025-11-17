import pytest
from user_api import UserAPI
from store_api import StoreAPI

BASE_URL = 'https://petstore.swagger.io/v2'

class TestPetStoreAPI:
    
    def setup_method(self):
        self.user_api = UserAPI(BASE_URL)
        self.store_api = StoreAPI(BASE_URL)
    
    def test_create_and_get_user(self):
        """Test user creation and retrieval"""
        user_data = {
            "id": 1,
            "username": "testuser",
            "firstName": "Test",
            "lastName": "User", 
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        
        create_result = self.user_api.create_user(user_data)
        assert create_result is not None
        
        get_result = self.user_api.get_user_by_username("testuser")
        assert get_result is not None
    
    def test_get_inventory(self):
        """Test inventory retrieval"""
        inventory = self.store_api.get_inventory()
        assert inventory is not None
        assert isinstance(inventory, dict)
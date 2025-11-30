import pytest
import time
from user_api import UserAPI
from store_api import StoreAPI

BASE_URL = 'https://petstore.swagger.io/v2'

class TestPetStoreComplete:
    
    def setup_method(self):
        self.user_api = UserAPI(BASE_URL)
        self.store_api = StoreAPI(BASE_URL)
        self.timestamp = int(time.time())
        self.username = f"testuser_{self.timestamp}"
        self.order_id = self.timestamp
    
    # USER API TESTS (4 теста)
    
    def test_create_user(self):
        """Test user creation - POST /user"""
        user_data = {
            "id": self.timestamp,
            "username": self.username,
            "firstName": "Test",
            "lastName": "User", 
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        
        result = self.user_api.create_user(user_data)
        assert result is not None
        print("User created successfully")
    
    def test_get_user(self):
        """Test get user by username - GET /user/{username}"""
        # Сначала создаем пользователя
        user_data = {
            "id": self.timestamp,
            "username": self.username,
            "firstName": "Test",
            "lastName": "User", 
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        self.user_api.create_user(user_data)
        
        # Затем получаем
        result = self.user_api.get_user_by_username(self.username)
        assert result is not None
        assert result.get('username') == self.username
        print("User retrieved successfully")
    
    def test_update_user(self):
        """Test update user - PUT /user/{username}"""
        # Сначала создаем
        user_data = {
            "id": self.timestamp,
            "username": self.username,
            "firstName": "Test",
            "lastName": "User", 
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        self.user_api.create_user(user_data)
        
        # Затем обновляем
        updated_data = {
            "id": self.timestamp,
            "username": self.username,
            "firstName": "Updated",
            "lastName": "User", 
            "email": "updated@example.com",
            "password": "newpassword456",
            "phone": "0987654321",
            "userStatus": 1
        }
        
        result = self.user_api.update_user(self.username, updated_data)
        assert result is not None
        print("User updated successfully")
    
    def test_delete_user(self):
        """Test delete user - DELETE /user/{username}"""
        # Сначала создаем
        user_data = {
            "id": self.timestamp,
            "username": self.username,
            "firstName": "Test",
            "lastName": "User", 
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        }
        self.user_api.create_user(user_data)
        
        # Затем удаляем
        result = self.user_api.delete_user(self.username)
        assert result is not None
        print("User deleted successfully")
    
    # STORE API TESTS (4 теста)
    
    def test_get_inventory(self):
        """Test inventory retrieval - GET /store/inventory"""
        inventory = self.store_api.get_inventory()
        assert inventory is not None
        assert isinstance(inventory, dict)
        print("Inventory retrieved successfully")
    
    def test_place_order(self):
        """Test place order - POST /store/order"""
        order_data = {
            "id": self.order_id,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2024-12-19T10:00:00.000Z",
            "status": "placed",
            "complete": True
        }
        
        result = self.store_api.place_order(order_data)
        assert result is not None
        assert result.get('id') == self.order_id
        print("Order placed successfully")
    
    def test_get_order(self):
        """Test get order by ID - GET /store/order/{orderId}"""
        # Сначала создаем заказ
        order_data = {
            "id": self.order_id,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2024-12-19T10:00:00.000Z",
            "status": "placed",
            "complete": True
        }
        self.store_api.place_order(order_data)
        
        # Затем получаем
        result = self.store_api.get_order_by_id(self.order_id)
        assert result is not None
        assert result.get('id') == self.order_id
        print("Order retrieved successfully")
    
    def test_delete_order(self):
        """Test delete order - DELETE /store/order/{orderId}"""
        # Сначала создаем заказ
        order_data = {
            "id": self.order_id,
            "petId": 1,
            "quantity": 1,
            "shipDate": "2024-12-19T10:00:00.000Z",
            "status": "placed",
            "complete": True
        }
        self.store_api.place_order(order_data)
        
        # Затем удаляем
        result = self.store_api.delete_order(self.order_id)
        assert result is not None
        print("Order deleted successfully")
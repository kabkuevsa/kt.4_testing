from user_api import UserAPI
from store_api import StoreAPI

BASE_URL = 'https://petstore.swagger.io/v2'

def test_user_api():
    print("=== USER API TESTS ===")
    user_api = UserAPI(BASE_URL)
    
    try:
        
        print("1. Create user - START")
        result = user_api.create_user({
            "id": 1,
            "username": "testuser",
            "firstName": "Test",
            "lastName": "User",
            "email": "test@example.com",
            "password": "password123",
            "phone": "1234567890",
            "userStatus": 1
        })
        print("1. Create user - COMPLETE")
        print(f"Result: {result}")
        
        
        print("2. Get user - START")
        result = user_api.get_user_by_username("testuser")
        print("2. Get user - COMPLETE")
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"ERROR: {e}")

def test_store_api():
    print("\n=== STORE API TESTS ===")
    store_api = StoreAPI(BASE_URL)
    
    try:
        
        print("1. Get inventory - START")
        result = store_api.get_inventory()
        print("1. Get inventory - COMPLETE")
        print(f"Result: {result}")
        
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    test_user_api()
    test_store_api()
    print("=== TESTS FINISHED ===")
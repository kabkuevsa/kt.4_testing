from base_request import BaseRequest

class UserAPI(BaseRequest):
    def __init__(self, base_url):
        super().__init__(base_url)
    
    def create_user(self, user_data):
        """Create user - POST /user"""
        return self.post("user", "", user_data)
    
    def get_user_by_username(self, username):
        """Get user by username - GET /user/{username}"""
        return self.get("user", username)
    
    def update_user(self, username, user_data):
        """Update user - PUT /user/{username}"""
        return self.put("user", username, user_data)  # ИСПРАВЛЕНО: post -> put
    
    def delete_user(self, username):
        """Delete user - DELETE /user/{username}"""
        return self.delete("user", username)
    
    def user_login(self, username, password):
        """User login - GET /user/login"""
        return self.get("user/login", f"?username={username}&password={password}")
    
    def user_logout(self):
        """User logout - GET /user/logout"""
        return self.get("user/logout", "")
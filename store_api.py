from base_request import BaseRequest

class StoreAPI(BaseRequest):
    def __init__(self, base_url):
        super().__init__(base_url)
    
    def get_inventory(self):
        """Get inventory - GET /store/inventory"""
        return self.get("store/inventory", "")
    
    def place_order(self, order_data):
        """Place order - POST /store/order"""
        return self.post("store/order", "", order_data)
    
    def get_order_by_id(self, order_id):
        """Get order by ID - GET /store/order/{orderId}"""
        return self.get("store/order", order_id)
    
    def delete_order(self, order_id):
        """Delete order - DELETE /store/order/{orderId}"""
        return self.delete("store/order", order_id)
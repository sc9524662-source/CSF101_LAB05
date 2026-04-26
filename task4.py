# testing the customer services
from collections import deque
class CustomerService:
    def __init__(self):
        self.queue = deque()
    
    def add_customer(self, name):
        self.queue.append(name)
        print(f"Added {name} to the queue")
    
    def serve_customer(self):
        if self.queue:
            served = self.queue.popleft()
            print(f"Serving customer: {served}")
        else:
            print("No customers waiting")
    
    def show_remaining(self):
        print(f"Remaining queue: {list(self.queue)}")

# Test the customer service system
if __name__ == "__main__":
    service = CustomerService()
    
    # Add customers
    service.add_customer("Sangay")
    service.add_customer("tashi")
    service.add_customer("Karma")
    
    print(f"\nCustomers waiting: {list(service.queue)}")
    
    # Serve customers
    service.serve_customer()
    service.show_remaining()
    
    service.serve_customer()
    service.show_remaining()
  
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete_node(self, data):
        if not self.head:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next
    
    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return f"Element found at position {position}"
            current = current.next
            position += 1
        return "Element not found"
    
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        elements.append("None")
        print(" -> ".join(elements))

# Test the linked list
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("Linked List:", end=" ")
    ll.display()
    
    ll.insert_at_beginning(5)
    print("After inserting 5 at beginning:", end=" ")
    ll.display()
    
    ll.delete_node(20)
    print("After deleting 20:", end=" ")
    ll.display()
    
    print(ll.search(30))
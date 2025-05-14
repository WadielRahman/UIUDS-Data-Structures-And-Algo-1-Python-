# Reverse a Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def show(self):
        temp = self.head
        print("Linked List: ")
        while temp:
            print(temp.data, end="-->")

            temp = temp.next
        print()

    def reverse_doubly(self):
        temp = self.head
        prev_node = None
    
        original_head = self.head
        while temp:
            temp.next, temp.prev = temp.prev, temp.next

            prev_node = temp

            temp = temp.prev

            
        self.head = prev_node
        self.tail = original_head


llst = LinkedList()
llst.insertAtEnd(1)
llst.insertAtEnd(2)
llst.insertAtEnd(3)
llst.insertAtEnd(5)
llst.insertAtEnd(5)
llst.insertAtEnd(6)
llst.insertAtEnd(7)
llst.insertAtEnd(10)

llst.reverse_doubly()
llst.show()
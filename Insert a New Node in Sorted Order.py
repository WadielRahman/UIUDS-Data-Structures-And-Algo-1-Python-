class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
    
    def insert_in_sorted_order(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        if new_data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        while temp.next != None and temp.next.data < new_node.data:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def show(self):
        temp = self.head
        print("Linked List: ")
        while temp:
            print(temp.data, end="-->")

            temp = temp.next
        print()

llst = LinkedList()
llst.insertAtEnd(1)
llst.insertAtEnd(2)
llst.insertAtEnd(3)
llst.insertAtEnd(5)
llst.insertAtEnd(5)
llst.insertAtEnd(6)
llst.insertAtEnd(7)
llst.insertAtEnd(10)

llst.insert_in_sorted_order(4)
llst.show()
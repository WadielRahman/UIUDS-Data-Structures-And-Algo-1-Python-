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

    def show(self):
        temp = self.head
        print("Linked List: ")
        while temp:
            print(temp.data, end="-->")

            temp = temp.next
        print()

    def delete_even(self):
        temp = self.head
        while temp.next:
            if temp.next.data % 2 == 0:
                temp.next = temp.next.next
            else:   
                temp = temp.next


llst = LinkedList()
llst.insertAtEnd(1)
llst.insertAtEnd(2)
llst.insertAtEnd(3)
llst.insertAtEnd(5)
llst.insertAtEnd(5)
llst.insertAtEnd(6)
llst.insertAtEnd(7)
llst.insertAtEnd(10)

llst.delete_even()
llst.show()
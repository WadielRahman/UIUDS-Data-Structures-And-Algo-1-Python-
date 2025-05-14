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
    
    def get_occurrence(self, target):
        count = 0
        temp = self.head
        while temp:
            if temp.data == target:
                count += 1
            temp = temp.next
        
        return count


llst = LinkedList()
llst.insertAtEnd(55)
llst.insertAtEnd(34)
llst.insertAtEnd(12)
llst.insertAtEnd(55)
llst.insertAtEnd(55)
llst.insertAtEnd(42)
llst.insertAtEnd(55)

print(llst.get_occurrence(55))
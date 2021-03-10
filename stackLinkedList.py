from node import Node
from linkedList import LinkedList

class StackLinkedList(object):

    def __init__(self):
        self.head = None
        self.maximum = LinkedList()

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.maximum.push(data)
        elif data > self.maximum.head.data:
            temp = (2 * data) - self.maximum.top().data
            newnode = Node(temp)
            newnode.next = self.head
            self.head = newnode
            self.maximum.push(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)
    def pop(self):

        if self.is_empty():
            return None

        else:
            removed_node = self.head.data
            self.head = self.head.next
            if removed_node > self.maximum.top().data:
                print ("Top Most Element Removed :{} " .format(self.maximum.top().data))
                self.maximum.push(((2 * self.maximum.top().data) - removed_node))
            else:
                print ("Top Most Element Removed : {}" .format(removed_node))

    # Returns the head node data
    def top(self):

        if self.is_empty():
            return None

        else:
            return self.head.data

    def get_max(self):
        if self.top is None:
            return "Stack is empty"
        else:
            print("Maximum Element in the stack is: {}" .format(self.maximum.top().data))

def main():
    stack = StackLinkedList()
    stack.push(5)
    stack.push(7)
    stack.push(3)
    stack.push(6)
    stack.get_max()
    stack.pop()
    stack.get_max()
    stack.pop()
    stack.get_max()
    stack.pop()
    stack.get_max()

if __name__ == "__main__":
    main()




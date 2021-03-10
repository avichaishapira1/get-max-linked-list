from node import Node


class LinkedList():

    def __init__(self):
        self.head = None
        self._len = 0

    def push(self, data):

        # If the list is empty, create a
        # single node circular and doubly list
        if (self.head == None) :

            new_node = Node(data)
            new_node.next = None
            self.head = new_node
            return

        # If list is not empty
        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

        # Create Node dynamically
        new_node = Node(data)

        # Start is going to be next of new_node
        new_node.next = None

        self._len += 1

    def pop(self):
        if self.head is None:
            print('Linked list is empty')
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next

    def top(self):
        return self.head


    def len(self):
        return self._len

    def display(self):
        temp = self.head

        print("Printing finished list:")
        while temp.next is not None:

            print(temp.data, end=" ")
            temp = temp.next





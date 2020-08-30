# Prasoon Shakya
# Class - CS 301 (Data Structure And Algorithms)
# Assignment #2
# Date : 03/12/2020
# Linked List file for the main source code which is then used for managing the waiting list in the program


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = node()

    # Adds a new node at the end of the list.
    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # Returns the get_length of the list i.e. number of nodes in the list
    def get_length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    # Returns the value contained in a node
    def get(self, index):
        current_indx = 0
        current_node = self.head
        while True:
            if current_indx == index:
                return current_node.data
            current_node = current_node.next
            current_indx += 1

    # Deletes the node of the particular index
    def remove(self, index):
        current_indx = 0
        current_node = self.head
        last_node = current_node
        while True:
            if current_indx == index:
                last_node.next = current_node.next
                return
            current_node = current_node.next
            current_indx += 1

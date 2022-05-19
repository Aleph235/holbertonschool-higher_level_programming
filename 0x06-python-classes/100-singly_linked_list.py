#!/usr/bin/python3
"""singly linked list class"""


class Node:
    """Defining a linked list node class"""
    def __init__(self, data, next_node=None):
        """initialisation of class members"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """member data getter function"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets data private member if if it is an integer"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """member next_node getter function"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value != None or type(value) != Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value

class SinglyLinkedList:
    """Defining a SinglyLinkedList class"""
    def __init__(self):
        """initializing attributes of class SinglyLinkedList"""
        self.__head = None

    def __str__(self):
        """make SinglyLinkedList printable"""
        return str(self)

    def sorted_insert(self, value):
        """insert sorted new node to SinglyLinkedList"""
        new_node = Node(value)

        if self.__head is None:
           new_node.next_node = self.__head
           self.__head = new_node

        elif self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            current = self.__head
            while(current.next != None and current.next.data < new_node.data):
                current = current.next

            new_node.next_node = current.next
            current.next_node = new_node


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

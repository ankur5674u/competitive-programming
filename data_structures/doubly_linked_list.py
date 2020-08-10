__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '08-09-2020'

import inspect


class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None

    def display(self):
        l_list = []
        temp = self.head
        while temp is not None:
            l_list.append(temp.data)
            temp = temp.next
        return l_list

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node is None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node

    def insert_after(self, node_data, data):
        pass

    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                return temp
            temp = temp.next
        return False

    def delete(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            temp = temp.next

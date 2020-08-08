__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '08-08-2020'

import inspect


class Node(object):
    """
        Node class for creating a node for linked list.
        Each node has its own data and a pointer that points
        to next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """
        :param data:
        :param next_node:
        """
        self.data = data
        self.next = next_node

    @staticmethod
    def get_code():
        return inspect.getsource(Node)


class LinkedListError(Exception):
    def __init__(self, message):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None

    def _search(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return node
        return self._search(node.next, data)

    def search(self, data):
        """
        This Function checks whether the value data present in the linked list
        :param data:
        :return:
        """
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def get_list(self):
        l_list = []
        temp = self.head
        while temp:
            l_list.append(temp.data)
            temp = temp.next
        return l_list

    def insert_at_beginning(self, data):
        """
        insert an item at the beginning of the linked list
        :param data:
        :return:
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            return self.insert_at_beginning(data)
        new_node = Node(data)
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def insert_node_after(self, node_data, data):
        current_node = self._search(self.head, node_data)
        if current_node is False:
            print(f"{node_data} does not exist in list")
            return None
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node

    def delete(self, data):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked list
        if temp is None:
            return

        # Unlink the node from linked list
        prev.next = temp.next

        temp = None

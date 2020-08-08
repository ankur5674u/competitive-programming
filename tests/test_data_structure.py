import unittest
import random

from data_structures import (
    linked_list
)


class TestLinkedList(unittest.TestCase):
    def test_singly_linked_list(self):
        list = linked_list.SinglyLinkedList()
        list.insert_at_beginning(3)
        list.insert_at_beginning(5)
        list.insert_at_beginning(2)
        list.insert_at_beginning(1)
        list.insert_at_beginning(4)
        list.insert_at_end(8)

        expected_result = [4, 1, 2, 5, 3, 8]
        self.assertEqual(list.get_list(), expected_result)
        # Checking search Function
        self.assertTrue(list.search(4))
        # Checking search function negative function
        self.assertFalse(list.search(12))

        # Checking insert_node_after
        self.assertEqual(list.insert_node_after(50, 70), None)
        list.insert_node_after(5, 6)
        self.assertEqual(list.get_list(), [4, 1, 2, 5, 6, 3, 8])
        # Delete node
        list.delete(4)
        self.assertEqual(list.get_list(), [1, 2, 5, 6, 3, 8])


if __name__ == '__main__':
    unittest.main()

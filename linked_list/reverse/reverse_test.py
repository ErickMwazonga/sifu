import unittest
from reverse import Node, LinkedList

class LinkedListTests(unittest.TestCase):
    def test_empty_list(self):
        linked_list = LinkedList()
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [])

    def test_one_node(self):
        linked_list = LinkedList(Node(1))
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [1])

    def test_multiple_nodes(self):
        linked_list = LinkedList(Node(1, Node(2, Node(3, Node(4)))))
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [4, 3, 2, 1])

    def test_double_reversal(self):
        linked_list = LinkedList(Node(1, Node(2, Node(3, Node(4)))))
        linked_list.reverse()
        linked_list.reverse()
        values = list(linked_list)
        self.assertListEqual(values, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main(verbosity=2)
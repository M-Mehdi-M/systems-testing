import unittest
from tree import Tree
from node import Node

class TestTree(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        for val in [5, 3, 8, 1, 4]:
            self.tree.add(val)

    def test_find_existing(self):
        node = self.tree._find(3, self.tree.getRoot())
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 3)

    def test_find_non_existing(self):
        node = self.tree._find(10, self.tree.getRoot())
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()

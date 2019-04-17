import unittest
import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import binary_tree


class TestHashTable(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAdd(self):
        bt = binary_tree.BinaryTree()
        bt.add(50)
        bt.add(17)
        bt.add(76)
        bt.add(9)
        bt.add(23)
        bt.add(14)
        bt.add(12)
        bt.add(54)
        bt.add(72)
        bt.add(67)
        self.assertEqual(bt.root.value, 50)
        self.assertEqual(bt.root.left.value, 17)
        self.assertEqual(bt.root.right.value, 76)
        self.assertEqual(bt.root.left.left.value, 9)
        self.assertEqual(bt.root.left.right.value, 23)
        self.assertEqual(bt.root.left.left.right.value, 14)
        self.assertEqual(bt.root.left.left.right.left.value, 12)
        self.assertEqual(bt.root.right.left.value, 54)
        self.assertEqual(bt.root.right.left.right.value, 72)
        self.assertEqual(bt.root.right.left.right.left.value, 67)

    def testFind(self):
        # Search all elements
        bt = binary_tree.BinaryTree()
        bt.add(50)
        bt.add(17)
        bt.add(76)
        bt.add(9)
        bt.add(23)
        self.assertEqual(bt.find(50), bt.root)
        self.assertEqual(bt.find(17), bt.root.left)
        self.assertEqual(bt.find(76), bt.root.right)
        self.assertEqual(bt.find(9), bt.root.left.left)
        self.assertEqual(bt.find(23), bt.root.left.right)

        # # Search when Tree is empty
        # bt = binary_tree.BinaryTree()
        # self.assertRaises(bt.find(50), KeyError)

    def testDelete(self):
        bt = binary_tree.BinaryTree()
        bt.add(50)
        bt.add(17)
        bt.add(76)
        bt.add(9)
        bt.add(23)
        bt.add(14)
        bt.add(12)
        bt.add(54)
        bt.add(72)
        bt.add(67)
        bt.delete(9)
        self.assertEqual(bt.root.left.left.value, 14)
        bt.delete(67)
        self.assertEqual(bt.root.right.left.right.left, None)
        bt.delete(76)
        self.assertEqual(bt.root.right.value, 54)


if __name__ == '__main__':
    unittest.main()

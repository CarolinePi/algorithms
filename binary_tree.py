class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.length = 0
        self.out = ''

    def add(self, value, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.length += 1
            self.root = Node(value)
        else:
            if value < node.value:
                if node.left is None:
                    temp = Node(value)
                    node.left = temp
                    self.length += 1
                else:
                    self.add(value, node.left)
            if value > node.value:
                if node.right is None:
                    temp = Node(value)
                    node.right = temp
                    self.length += 1
                else:
                    self.add(value, node.right)

    def find(self, value, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            print('Binary Tree is empty!')
        else:
            if value < node.value:
                if node.left is not None:
                    return self.find(value, node.left)
                else:
                    print(str(value) + ' is not found')
                    return None
            elif value > node.value:
                if node.right is not None:
                    return self.find(value, node.right)
                else:
                    print(str(value) + ' is not found')
                    return None
            elif value == node.value:
                print(str(value) + ' is found!')
                return node

    def minimum_in_branch(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, value, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            print('Binary Tree is empty!')
        else:
            if value < node.value:
                node.left = self.delete(value, node.left)
            elif value > node.value:
                node.right = self.delete(value, node.right)
            else:
                if node.left is None:
                    temp = node.right
                    node = None
                    return temp
                elif node.right is None:
                    temp = node.left
                    node = None
                    return temp
                temp = self.minimum_in_branch(node.right)
                node.key = temp.value
                node.right = self.delete(temp.value, node.right)
            return node

    def __str__(self, node=None):
        if self.root is None:
            return '[]'
        if node is None:
            node = self.root
        if node.left is not None:
            self.__str__(node.left)
        self.out += str(node.value) + ' '
        if node.right is not None:
            self.__str__(node.right)
        return self.out

if __name__ == "__main__":
    # Run unit tests
    import unittest
    suite = unittest.defaultTestLoader.discover('./unit-test', pattern='binary_tree_test.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)


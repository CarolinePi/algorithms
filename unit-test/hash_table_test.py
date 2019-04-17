import unittest
import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import hash_table


class TestHashTable(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreate(self):
        ht = hash_table.HashTable(5)
        self.assertEqual(ht._size, 5)
        self.assertEqual(ht.table, [[None], [None], [None], [None], [None]])

        ht = hash_table.HashTable(8)
        self.assertEqual(ht._size, 8)
        self.assertEqual(ht.table, [[None], [None], [None], [None], [None], [None], [None], [None]])

    def testAdd(self):
        # Simple add two elements
        ht = hash_table.HashTable(5)
        array = [[None], [None], [None], [None], [None]]
        ht.add('Bob', '567-8888')
        ht.add('Ankit', '293-8625')
        if ht._get_hash('Bob') != ht._get_hash('Ankit'):
            array[ht._get_hash('Bob')] = [['Bob', '567-8888']]
            array[ht._get_hash('Ankit')] = [['Ankit', '293-8625']]
        else:
            array[ht._get_hash('Bob')] = [['Bob', '567-8888'], ['Ankit', '293-8625']]
        self.assertEqual(ht.table, array)

        # Add two elements with substitution value
        ht = hash_table.HashTable(5)
        array = [[None], [None], [None], [None], [None]]
        ht.add('Bob', '567-8888')
        ht.add('Ankit', '293-8625')
        ht.add('Ankit', '293-6753')
        if ht._get_hash('Bob') != ht._get_hash('Ankit'):
            array[ht._get_hash('Bob')] = [['Bob', '567-8888']]
            array[ht._get_hash('Ankit')] = [['Ankit', '293-6753']]
        else:
            array[ht._get_hash('Bob')] = [['Bob', '567-8888'], ['Ankit', '293-6753']]
        self.assertEqual(ht.table, array)


if __name__ == '__main__':
    unittest.main()

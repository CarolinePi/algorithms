class HashTable:
    def __init__(self, size):
        self._size = size
        self.table = [[None]] * self._size

    def _get_hash(self, key):
        return hash(key) % self._size

    def add(self, key, value):
        hash_key = self._get_hash(key)
        if self.table[hash_key] != [None]:
            for iterator in self.table[hash_key]:
                if iterator[0] == key:
                    iterator[1] = value
                    break
            else:
                self.table[hash_key].append([key, value])
        elif self.table[hash_key] == [None]:
            self.table[hash_key] = [[key, value]]

    def search(self, key):
        hash_key = self._get_hash(key)
        if self.table[hash_key] == [None]:
            raise KeyError()
        else:
            for iterator in self.table[hash_key]:
                if iterator[0] == key:
                    return str(iterator[1])
            else:
                raise KeyError()

    def delete(self, key):
        hash_key = self._get_hash(key)
        if self.table[hash_key] == [None]:
            raise KeyError()
        else:
            for k, iterator in enumerate(self.table[hash_key]):
                if iterator[0] == key:
                    del self.table[hash_key][k]
                    if len(self.table[hash_key]) == 0:
                        self.table[hash_key] = [None]
                    break


# h = HashTable(3)
# h.add('Bob', '567-8888')
# h.add('Ming', '293-6753')
# h.add('Mike', '567-2188')
# print(h.table)
# h.delete('Bob')
# print(h.table)
# h.delete('Ming')
# print(h.table)
# h.delete('Mike')
# print()
# print('Ming: ' + h.search('Ming'))
# print('Aditya: ' + h.search('Aditya'))
# print()
# print(h.table)


if __name__ == "__main__":
    # Run unit tests
    import unittest
    suite = unittest.defaultTestLoader.discover('./unit-test', pattern='hash_table_test.py')
    runner = unittest.TextTestRunner()
    runner.run(suite)



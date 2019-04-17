class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.begin = None
        self.end = None
        self._length = 0

    def __str__(self):
        if self.begin is not None:
            current = self.begin
            out = '[' + str(current.data)
            while current.next is not None:
                current = current.next
                out += ', ' + str(current.data)
            return out + ']'
        return '[]'

    def clean(self):
        self.__init__()

    def insert_to_end(self, data):
        self._length += 1
        if self.begin is None:
            self.begin = self.end = Node(None, data, None)
        else:
            self.end.next = self.end = Node(self.end, data, None)

    def insert_to_begin(self, data):
        self._length += 1
        if self.begin is None:
            self.begin = self.end = Node(None, data, None)
        else:
            self.begin = Node(None, data, self.begin)

    def insert_to_center(self, data, index):
        if index < self._length:
            self._length += 1
            current = self.begin
            for _ in range(1, index):
                current = current.next
            current.next = Node(current, data, current.next)
        else:
            raise IndexError()

    def remove_to_end(self):
        if self._length == 0:
            print('Nothing can`t be removed')
        else:
            current = self.begin
            self._length -= 1
            for _ in range(self._length - 2):
                current = current.next
            current.next = Node(current, current.next.data, None)

    def remove_to_begin(self):
        if self._length == 0:
            print('Nothing can`t be removed')
        else:
            self._length -= 1
            current = self.begin
            self.begin = current.next

    def remove_to_center(self, index):
        if self._length == 0:
            print('Nothing can`t be removed')
        else:
            current = self.begin
            self._length -= 1
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next

    def replace_to_begin(self, data):
        self.begin = Node(None, data, self.begin.next)

    def replace_to_center(self, data, index):
        current = self.begin
        for _ in range(index - 1):
            current = current.next
        current.next = Node(current.next, data, current.next.next)

    def replace_to_end(self, data):
        current = self.begin
        for _ in range(self._length - 1):
            current = current.next
        current.data = data

    def __getitem__(self, key):
        count = 0
        if key > self._length - 1:
            raise IndexError()
        else:
            if self.begin is not None:
                current = self.begin
                while count != key:
                    current = current.next
                    count += 1
                print(current.data)
                
    def get_length(self):
        print(self._length)


s = DoubleLinkedList()
s.insert_to_end(3)
s.insert_to_end(2)
s.insert_to_begin(1)
s.insert_to_begin(4)
s.insert_to_begin(4)
s.insert_to_center(5, 3)
s.remove_to_end()
s.remove_to_begin()
s.remove_to_center(1)
s.insert_to_center(7, 2)
s.insert_to_center(3, 2)
s.remove_to_center(2)
s.replace_to_begin(2)
s.replace_to_center(4, 2)
s.replace_to_end(9)
s[1]
s.get_length()
print(s)

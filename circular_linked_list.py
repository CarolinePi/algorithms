class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.begin = None
        self._length = 0

    def __str__(self):
        if self.begin is not None:
            a = self.begin
            out = '[' + str(a.data)
            while a.next is not self.begin:
                a = a.next
                out += ', ' + str(a.data)
            return out + ']'
        return '[]'

    def clean(self):
        self.__init__()

    def insert_to_begin(self, data):
        self._length += 1
        temp = Node(data, self.begin)
        current = self.begin
        if self.begin is not None:
            while current.next != self.begin:
                current = current.next
            current.next = temp
        else:
            temp.next = temp
        self.begin = temp

    def insert_to_end(self, data):
        self._length += 1
        temp = Node(data, self.begin)
        current = self.begin
        if self.begin is not None:
            while current.next != self.begin:
                current = current.next
            current.next = temp
        else:
            temp.next = temp
            self.begin = temp

    def insert_to_center(self, data, index):
        if index < self._length:
            self._length += 1
            current = self.begin
            for _ in range(index - 1):
                current.next = Node(data, current.next)
        else:
            raise IndexError()

    def remove_to_end(self):
        if self._length == 0:
            print('Nothing can`t be removed')
        else:
            current = self.begin
            self._length -= 1
            for _ in range(self._length - 1):
                current = current.next
            current.next = self.begin

    def remove_to_begin(self):
        if self._length == 0:
            print('Nothing can`t be removed')
        else:
            self._length -= 1
            self.begin = self.begin.next
            current = self.begin
            for _ in range(self._length - 1):
                current = current.next
            current.next = self.begin

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
        self.begin.data = data

    def replace_to_center(self, data, index):
        current = self.begin
        for _ in range(index - 1):
            current = current.next
        current.next = Node(data, current.next.next)

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


s = CircularLinkedList()

s.insert_to_begin(1)
s.insert_to_begin(4)
s.insert_to_end(3)
s.insert_to_end(2)
s.insert_to_center(5, 2)
s.remove_to_begin()
s.replace_to_begin(2)
s.replace_to_center(2, 2)
s.replace_to_end(4)
s.remove_to_center(2)
s.remove_to_end()
s[1]
s.get_length()
print(s)

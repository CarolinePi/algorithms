class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.__begin = None
        self.__length = 0

    def __str__(self):
        if self.__begin is not None:
            current = self.__begin
            out = '[' + str(current.data)
            while current.next is not None:
                current = current.next
                out += ', ' + str(current.data)
            return out + ']'
        return '[]'

    def clean(self):
        self.__init__()

    def push(self, data):
        if self.__begin is None:
            self.__begin = Node(data)
        else:
            new = Node(data)
            new.next = self.__begin
            self.__begin = new

    def pop(self):
        temp = self.__begin.data
        self.__begin = self.__begin.next
        return temp

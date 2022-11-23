class Node:
    def __init__(self, value,
                 prev_pointer=None, next_pointer=None):
        self.set_value(value)
        self.set_prev(prev_pointer)
        self.set_next(next_pointer)

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next_pointer

    def get_prev(self):
        return self._prev_pointer

    def set_value(self, value):
        self._value = value

    def set_prev(self, prev_pointer):
        self._prev_pointer = prev_pointer

    def set_next(self, next_pointer):
        self._next_pointer = next_pointer

    def __str__(self):
        return str(self.get_value())


class List:
    def __init__(self, collection = None):
        self._start_pointer = None
        self._finish_pointer = None
        self._length = 0

        # initialization with some collection structure
        if collection != None:
            for el in collection:
                self.append(el)

    def __len__(self):
        return self._length

    def append(self, value):
        if self._length == 0:
            self._start_pointer = Node(value)
            self._finish_pointer = self._start_pointer
            self._length = 1
        else:
            self._finish_pointer.set_next(Node(value,
                                               self._finish_pointer))
            self._finish_pointer = self._finish_pointer.get_next()
            self._length += 1

    def __getitem__(self, i):
        if i < 0 or i >= self._length:
            return False

        # select an element using
        # not more than ceil(N / 2) operations
        if i <= self._length // 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
        else:
            curr_pointer = self._finish_pointer
            for j in range(self._length - i - 1):
                curr_pointer = curr_pointer.get_prev()
        return curr_pointer.get_value()

    def __str__(self):
        arr = []
        for i in range(self._length):
            arr.append(str(self[i]))
        return "[" + ", ".join(arr) + "]"

    # addition operator overloaded for my lists
    def __add__(self, L):
        res = List()
        for i in range(len(self)):
            res.append(self[i])
        for i in range(len(L)):
            res.append(L[i])
        return res

    # remove an element from the list
    def pop(self, i):
        if i < 0 or i >= self._length:
            return False

        self._length -= 1

        if i == 0:
            self._start_pointer = self._start_pointer.get_next()
            self._start_pointer.set_prev(None)
            return True

        if i == self._length: # not length - 1 because it was decreased
            self._finish_pointer = self._finish_pointer.get_prev()
            self._finish_pointer.set_next(None)
            return True

        if i <= self._length // 2:
            curr_pointer = self._start_pointer
            for j in range(i):
                curr_pointer = curr_pointer.get_next()
        else:
            curr_pointer = self._finish_pointer
            for j in range(self._length - i - 1):
                curr_pointer = curr_pointer.get_prev()

        curr_pointer.get_prev().set_next(curr_pointer.get_next())

        return True

A = List((1, 2, 3, 4, 5))
B = List([6, 7, 8, 9, 10])
print(A)
print(B)
S = A + B
print(S)
print(S[0])
print(S[1])
print(S[8])
print(S[9])
S.pop(0)
print(S)
S.pop(8)
print(S)
S.pop(3)
print(S)

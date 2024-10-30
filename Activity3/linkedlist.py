class LinkedNode:
    def __init__(self,val):
        self._val = val
        self._next = None

    def get_val(self):
        return self._val

    def set_val(self, val):
        self._val = val

    def get_next(self):
        return self._next

    def set_next(self,next_node):
        self._next = next_node

    def __str__(self):
        return str(self._val)

class LinkedList:
    def __init__(self,limit_size = float('inf')):
        self._head = None
        self._limit_size = limit_size
        self._size = 0

    def is_empty(self):
        return self._head is None

    def is_full(self):
        return self._size >= self._limit_size

    def __str__(self):
        if self.is_empty():
            return print(f'List is empty')

        current_nodes = []
        pointer = self._head
        while pointer is not None:
            current_nodes.append(str(pointer))
            pointer = pointer.get_next()
        return " -> ".join(current_nodes)

    def search(self,val):
        if self.is_empty(): return print(f'This linked list is empty')

        pointer = self._head

        while pointer.get_next() is not None:
            if pointer.get_val() == val: return True

            else:
                pointer = pointer.get_next()

        return False

    def insert(self,val):
        if self.is_full():
            print(f'List is full, you cannot link more node')
            return

        node = LinkedNode(val)

        if self.is_empty():
            self._head = node

        else:
            pointer = self._head
            while pointer.get_next() is not None:
                pointer = pointer.get_next()
            pointer.set_next(node)
        self._size += 1


    def delete(self,target_val):

        pointer = self._head

        if pointer.get_val() == target_val:
            self._head = pointer.get_next
            pointer.set_next(None)
            return

        while pointer.get_next() is not None:
            if pointer.get_next().get_val() == target_val:
                break

            else:
                pointer = pointer.get_next()

        if pointer.get_next() is None: return print(f'there is not value {target_val}')

        elif pointer.get_next() is not None and pointer.get_next().get_next() is not None:
            pointer.set_next(pointer.get_next().get_next())

        elif pointer.get_next() is not None and pointer.get_next().get_next() is None:
            pointer.set_next(None)


    def traverse(self):
        if self.is_empty():
            return print(f'List is empty')

        current_nodes = []
        pointer = self._head
        while pointer is not None:
            current_nodes.append(str(pointer.get_val()))
            pointer = pointer.get_next()
        return " -> ".join(current_nodes)


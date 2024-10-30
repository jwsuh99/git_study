class TreeNode:
    def __init__(self,val):
        self._val = val
        self._left = None
        self._right = None

    def set_val(self,val):
        self._val = val

    def get_val(self):
        return self._val

    def get_left(self):
        return self._left

    def set_left(self,node):
        self._left = node

    def get_right(self):
        return self._right

    def set_right(self,node):
        self._right = node

class BinarySearchTree:
    def __init__(self, limit_size = float('inf')):
        self._root = None
        self._limit_size = limit_size

    def get_root(self):
        return self._root

    def set_root(self, node):
        self._root = node

    def is_empty(self):
        return self.get_root() is None

    def is_full(self):
        return self.get_size(self._root) >= self._limit_size

    def get_size(self,node): ##I reference https://www.geeksforgeeks.org/binary-tree-data-structure/ this site
        if node is None: return 0
        left = self.get_size(node.get_left())
        right = self.get_size(node.get_right())
        return left + right + 1

    def search_val(self, val):
        return self.search(self.get_root(),val)

    def search(self,node,val):
        if node is None: return False

        if node.get_val() == val: return True

        elif val < node.get_val(): return self.search(node.get_left(),val)

        else: return self.search(node.get_right(),val)

    def insert(self,val):
        if self._root is None:
            self._root = TreeNode(val)
            return

        node = TreeNode(val)

        if self.is_full():
            print(f'Tree is full')
            return
        current_node = self._root

        while True:
            if val < current_node.get_val():
                if current_node.get_left() is None:
                    current_node.set_left(node)
                    break
                else:current_node = current_node.get_left()

            else:
                if current_node.get_right() is None:
                    current_node.set_right(node)
                    break
                else:
                    current_node = current_node.get_right()

    def delete(self,node, val):
        if node is None:
            return node

        if val < node.get_val(): node.set_left(self.delete(node.get_left(), val))

        elif val > node.get_val(): node.set_right(self.delete(node.get_right(),val))

        else:
            if node.get_left() is None:
                temp_node = node.get_right()
                node = None
                return temp_node
            elif node.right is None:
                temp_node = node.get_left()
                node = None
                return temp_node

            temp = self.find_min(node.get_right())
            node.set_val(temp.get_val())
            node.set_right(self.delete(node.get_right(),temp.get_val()))
        return node

    def delete_val(self,val): #for a case we delete root
        self._root = self.delete(self._root,val)

    def find_min(self,node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def traverse(self,node): #dfs in - order
        if node is None:
            node = self._root

        if node is not None:
            self.traverse(node.get_left())
            print(node.val)
            self.traverse(node.get_right())

    def print_tree(self, node = None, depth = 0):
        if node is None:
            node = self._root
            if node is None: return

        if node.get_right():
            self.print_tree(node.get_right(), depth + 1)

        print('     ' * depth + f'-> {node.get_val()}')

        if node.get_left():
            self.print_tree(node.get_left(), depth + 1)



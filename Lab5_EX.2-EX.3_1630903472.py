class Treenode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class binary_tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Treenode(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Treenode(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Treenode(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value is already in the tree!")

    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        if data == cur_node.data:
            return True

    def max_height(self):
        if self.root:
            return self._max_height(self.root, 0)
        else:
            return 0

    def _max_height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._max_height(cur_node.left, cur_height + 1)
        right_height = self._max_height(cur_node.right, cur_height + 1)
        return max(left_height, right_height)

    def find_parent(self, data):
        if self.root:
            return self._find_parent(data, self.root)
        else:
            return None

    def _find_parent(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            if data == cur_node.right.data:
                return cur_node.data
            else:
                return self._find_parent(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            if data == cur_node.left.data:
                return cur_node.data
            else:
                return self._find_parent(data, cur_node.left)
        else:
            return None

    def find_children(self, data):
        if self.root:
            return self._find_children(data, self.root)
        else:
            return None

    def _find_children(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            if data == cur_node.data:
                return cur_node.right.data
            else:
                return self._find_children(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            if data == cur_node.data:
                return cur_node.left.data
            else:
                return self._find_children(data, cur_node.left)
        else:
            return None

    def find_leaves(self, data):
        if self.root:
            return self._find_leaves(data, self.root)
        else:
            return None

    def _find_leaves(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            if data == cur_node.data:
                return cur_node.right.data
            else:
                return self._find_leaves(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            if data == cur_node.data:
                return cur_node.left.data
            else:
                return self._find_leaves(data, cur_node.left)
        else:
            return None

    def find_sibling(self, data):
        if self.root:
            return self._find_sibling(data, self.root)
        else:
            return None

    def _find_sibling(self, data, cur_node):
        if data > cur_node.data and cur_node.right:
            if data == cur_node.right.data:
                return cur_node.left.data
            else:
                return self._find_sibling(data, cur_node.right)
        elif data < cur_node.data and cur_node.left:
            if data == cur_node.left.data:
                return cur_node.right.data
            else:
                return self._find_sibling(data, cur_node.left)
        else:
            return None

    def delete(self, data):
        if self.root is None:
            return False
        # Find node to remove
        parent = None
        node = self.root
        while node and node.data != data:
            parent = node
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
        if node is None or node.data != data:
            return False
        # Get children count
        children_count = 0
        if node.left:
            children_count += 1
        if node.right:
            children_count += 1
        # Remove node
        if children_count == 0:
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None
        elif children_count == 1:
            next_node = None
            if node.left:
                next_node = node.left
            else:
                next_node = node.right
            if parent:
                if parent.left is node:
                    parent.left = next_node
                else:
                    parent.right = next_node
            else:
                self.root = next_node
        else:
            parent = node
            next_node = node.right
            while next_node.left:
                parent = next_node
                next_node = next_node.left
            node.data = next_node.data
            if parent.left == next_node:
                parent.left = next_node.right
            else:
                parent.right = next_node.right
        return True


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def getcol(h):
    if h == 1:
        return 1
    return getcol(h - 1) + getcol(h - 1) + 1


def printTree(M, root, col, row, height):
    if root is None:
        return
    M[row][col] = root.data
    printTree(M, root.left, col - pow(2, height - 2), row + 1, height - 1)
    printTree(M, root.right, col + pow(2, height - 2), row + 1, height - 1)


def TreePrinter():
    h = height(tree.root)
    col = getcol(h)
    M = [[0 for _ in range(col)] for __ in range(h)]
    printTree(M, tree.root, col // 2, 0, h)
    for i in M:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print("")


print("Binary tree")
tree = binary_tree()
tree.root = Treenode(50)
data = [25, 75, 30, 60, 40, 35, 70, 90, 15, 45, 27, 55, 85, 100]
for i in data:
    tree.insert(i)
TreePrinter()
print("")
# delete
print("Delete 30")
tree.delete(30)
TreePrinter()
print("")
print("Delete 75")
tree.delete(75)
TreePrinter()
print("")
print("Delete 35")
tree.delete(35)
TreePrinter()
print("")
# find max height
print("Max height: ", height(tree.root))
# find parent
print("Parent of 45: ", tree.find_parent(45))
# find children
print("Children of 45: ", tree.find_children(45))
# find leaves
print("Leaves of 45: ", tree.find_leaves(45))
# find sibling
print("Sibling of 45: ", tree.find_sibling(45))

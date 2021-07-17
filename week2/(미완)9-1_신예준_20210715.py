import sys
sys.setrecursionlimit(10 ** 6)
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
class BinarySearchTree(Node):
    def __init__(self, root):
        self.root = root
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)

r = int(sys.stdin.readline())
root = Node(r)
bst = BinarySearchTree(root)
while True:
    try:
        x = int(sys.stdin.readline())
        bst.insert(x)
    except:
        break
bst.post_order_traversal()




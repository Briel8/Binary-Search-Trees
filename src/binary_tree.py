from src.node import Node

class Tree:
    def __init__(self, array):
        self.root = self.build_tree(sorted(set(array)))

    def build_tree(self, array):
        if not array:
            return None

        mid = len(array) // 2
        root = Node(array[mid])

        root.left = self.build_tree(array[ :mid])
        root.right = self.build_tree(array[mid+1: ])
        return root
    
    def find(self, value, node=None):
        if node is None:
            node = self.root
        if value < node.data:
            if node.left is None:
                return None
            else:
                return self.find(value, node.left)
        elif value > node.data:
            if node.right is None:
                return None
            else:
                return self.find(value, node.right)
        else:
            return node.data
        
    # define the level_order method

    def inorder(self, node=None, result=[]):
        if node is None:
            node = self.root
        if node is None:
            return None
        if node.left:
            self.inorder(node.left, result)
        result.append(node.data)
        if node.right:
            self.inorder(node.right, result)
        return result 

    def preorder(self, node=None, result=[]):
        if node is None:
            node = self.root
        if node is None:
            return None
        result.append(node.data)
        if node.left:
            self.preorder(node.left, result)
        if node.right:
            self.preorder(node.right, result)
        return result
    
    def postorder(self, node=None, result=[]):
        if node is None:
            node = self.root
        if node is None:
            return None
        if node.right:
            self.postorder(node.right, result)
        if node.left:
            self.postorder(node.left, result)
        result.append(node.data)
        return result

    def pretty_print(self, node, prefix='', is_left=True):
        if node.right:
            self.pretty_print(node.right, f"{prefix}{'|  ' if is_left else '   '}", False)
        print(f"{prefix}{'└──' if is_left else '┌──'}{node.data}")
        if node.left:
            self.pretty_print(node.left, f"{prefix}{'|  ' if is_left else '   '}", True)
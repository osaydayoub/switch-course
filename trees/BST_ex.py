# instructions
# implement the Node Class
# implement the get_max function

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    pass

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def get_max(self):
        """Returns the node with the maximum key in the BST."""
        if self.root == None:
            return None
        current_max_node = self.root
        while current_max_node.right:
            current_max_node = current_max_node.right
        return current_max_node

    def get_height(self):
        """Returns the height of the BST."""
        def height(node):
            if node is None:
                return -1
            else:
                return 1 + max(height(node.left),height(node.right))
        return height(self.root)
    
    def delete(self, value):
        self.root = self._delete_rec(self.root,value)
    
    def _delete_rec(self,node,value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_rec(node.left,value)
            return node
        
        if value > node.value:
            node.right = self._delete_rec(node.right,value)
            return node
        
        if node.left is None and node.right is None:
            return None
        
        if node.left is None:
            return node.right
        
        if node.right is None:
            return node.left
        
        successor = self.__min_node(node.right)
        node.value = successor.value
        node.right = self._delete_rec(node.right,successor.value)
        return node
        
    def __min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        
# Problem: Determine if Two Binary Search Trees (BSTs) are equivalent
# You are given the root nodes of two binary search trees (BSTs). 
# The task is to determine if the two trees are equivalent, regardless of the structure of the trees. 
# Meaning that each value that exists in one tree exists in the other tree and vice versa.  

def inorder(node , arr):
    if node is None:
        return 
    inorder(node.left,arr)
    arr.append(node.value)
    inorder(node.right,arr)

def are_bsts_equivalent(root1, root2):
    arr1 = []
    arr2 = []
    inorder(root1,arr1)
    inorder(root2,arr2)
    return arr1 == arr2



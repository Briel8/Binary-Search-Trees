class Node:
    """Represent a single node for a Tree data structure."""
    def __init__(self, value=None):
        self.data  = value
        self.left = None
        self.right = None
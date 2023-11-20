class Node:
    def __init__(self, value):
        self.root = value
        self.right = None
        self.left = None

    def insert(self, value):
        if self.root:
            if value > self.root:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
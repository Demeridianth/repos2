class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None
    
    def traverse_in_order(self, root):
        if root:
            self.traverse_in_order(root.left)
            print(root.data)
            self.traverse_in_order(root.right)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()


    def search(self, data):
        if data == self.data:
            return f'{data} is found in tree' 
        elif data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return f'{data} is not found in tree'
        else:
            if self.right:
                return self.right.search(data)
            else:
                return f'{data} is not found in tree'
            

root = Node(10)
# Tree Structure
#        10
#      /    \
#     None   None

root.left = Node(34)
root.right = Node(89)
root.left.left = Node(20)
root.left.right = Node(45)
root.right.right = Node(54)
root.right.left = Node(2)


# For the tree,
#          10
#        /    \
#       34      89
#     /    \  /    \
#  20     45  2    54

# root.traverse_in_order(root)
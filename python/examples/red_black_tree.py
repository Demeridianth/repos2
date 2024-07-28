# 1. Every node is either red or black.
# 2. The root is black.
# 3. Every leaf (NIL) is black.
# 4. If a node is red, then both its children are black.
# 5. For each node, all simple paths from the node to descendant leaves contain the
# same number of black nodes.
#  time complexity (сложность алгоритма) O(log n)


class RedBlackTree:

    RED = 1
    BLACK = 0

    class Node:
        """Node of the Red-Black Tree."""
        def __init__(self, val) -> None:
            self.val = val
            self.parent = None
            self.left = None
            self.right = None
            self.color = 1


    def __init__(self) -> None:
        """Initialize the Red-Black Tree."""
        self.NIL = self.Node(None)           # self.NIL = SENTINEL NODE !
        self.NIL.color = self.BLACK
        self.NIL.left = None
        self.NIL.right = None
        self.root = self.NIL
       
    def insert_node(self, key):
        """Insert a NEW NODE"""
        node = self.Node(key)
        node.parent = None
        node.val = key
        node.left = self.NIL
        node.right = self.NIL
        node.color = self.RED

        y = None
        x = self.root

        while x != self.NIL:                # Find position for new node
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right

        node.parent = y                     # Set parent of node as y
        if y == None:                       # If parent is none; it is ROOT
            self.root = node
        elif node.val < y.val:              # Check if it is a right node or a left node
            y.left = node
        else:
            y.right = node

        if node.parent == None:             # Root node is always Black
            node.color = self.BLACK
            return None
        
        if node.parent.parent == None:      # if parent of node is Root
            return None
        
        else:
            self.fix_insert(node)           # Else call for a fix up


    def find_minimum(self, node):
        """Find node with minimum val"""
        while node.left != self.NIL:
            node = node.left
        return node
    
    def rotation_to_left(self, x):
        """Rotation to the left"""
        y = x.right                         # Y = Right child of x
        x.right = y.left                    # Change right child of x to left child of y
        if y.left != self.NIL :
            y.left.parent = x

        y.parent = x.parent                 # Change parent of y as parent of x
        if x.parent == None :               # If parent of x == None:
            self.root = y                   # Set y as root
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotation_to_right(self , x) :
        """Rotation to the right"""
        y = x.left                          # Y = Left child of x
        x.left = y.right                    # Change left child of x to right child of y
        if y.right != self.NIL :
            y.right.parent = x

        y.parent = x.parent                 # Change parent of y as parent of x
        if x.parent == None :               # If x is root node
            self.root = y                   # Set y as root
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        """Method to fix an inserted node in order to maintain the Red-Black Tree Property"""
        while k.parent.color == 1:                        # While parent is red
            if k.parent == k.parent.parent.right:         # if parent is right child of its parent
                u = k.parent.parent.left                  # Left child of grandparent
                if u.color == 1:                          # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set both children of grandparent node as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # Set grandparent node as Red
                    k = k.parent.parent                   # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.parent.left:                # If k is left child of it's parent
                        k = k.parent
                        self.rotation_to_right(k)                        # Call for right rotation
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotation_to_left(k.parent.parent)
            else:                                         # if parent is left child of its parent
                u = k.parent.parent.right                 # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    k.parent.color = 0
                    k.parent.parent.color = 1             # set color of grandparent as Red
                    k = k.parent.parent                   # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.parent.right:               # if k is right child of its parent
                        k = k.parent
                        self.rotation_to_left(k)                        # Call left rotate on parent of k
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rotation_to_right(k.parent.parent)              # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                break
        self.root.color = 0   

    def fix_delete(self, x) :
        """Method to fix after deletion in order to maintain the Red-Black Tree Property"""
        while x != self.root and x.color == 0 :           # Repeat until x reaches nodes and color of x is black
            if x == x.parent.left :                       # If x is left child of its parent
                s = x.parent.right                        # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.parent.color = 1                    # Make its parent red
                    self.rotation_to_left(x.parent)                  # Call for left rotate on parent of x
                    s = x.parent.right
                # If both the child are black
                if s.left.color == 0 and s.right.color == 0 :
                    s.color = 1                           # Set color of s as red
                    x = x.parent
                else :
                    if s.right.color == 0 :               # If right child of s is black
                        s.left.color = 0                  # set left child of s as black
                        s.color = 1                       # set color of s as red
                        self.rotation_to_right(s)                     # call right rotation on x
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0                    # Set parent of x as black
                    s.right.color = 0
                    self.rotation_to_left(x.parent)                  # call left rotation on parent of x
                    x = self.root
            else :                                        # If x is right child of its parent
                s = x.parent.left                         # Sibling of x
                if s.color == 1 :                         # if sibling is red
                    s.color = 0                           # Set its color to black
                    x.parent.color = 1                    # Make its parent red
                    self.rotation_to_right(x.parent)                  # Call for right rotate on parent of x
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0 :
                    s.color = 1
                    x = x.parent
                else :
                    if s.left.color == 0 :                # If left child of s is black
                        s.right.color = 0                 # set right child of s as black
                        s.color = 1
                        self.rotation_to_left(s)                     # call left rotation on x
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rotation_to_right(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v) :
        """Function to transplant nodes"""
        if u.parent == None :
            self.root = v
        elif u == u.parent.left :
            u.parent.left = v
        else :
            u.parent.right = v
        v.parent = u.parent

    def delete_node_helper(self, node, key) :
        """Method for handling deletion"""
        z = self.NIL
        while node != self.NIL :                          # Search for the node having that value/ key and store it in 'z'
            if node.val == key :
                z = node

            if node.val <= key :
                node = node.right
            else :
                node = node.left

        if z == self.NIL :                                # If Kwy is not present then deletion not possible so return
            print("Value not present in Tree !!")
            return

        y = z
        y_original_color = y.color                          # Store the color of z- node
        if z.left == self.NIL :                            # If left child of z is NIL
            x = z.right                                     # Assign right child of z to x
            self.__rb_transplant(z ,z.right)            # Transplant Node to be deleted with x
        elif (z.right == self.NIL) :                       # If right child of z is NIL
            x = z.left                                      # Assign left child of z to x
            self.__rb_transplant(z ,z.left)             # Transplant Node to be deleted with x
        else :                                              # If z has both the child nodes
            y = self.minimum (z.right)                    # Find minimum of the right sub tree
            y_original_color = y.color                      # Store color of y
            x = y.right
            if y.parent == z :                              # If y is child of z
                x.parent = y                                # Set parent of x as y
            else :
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z , y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0 :                          # If color is black then fixing is needed
            self.fix_delete(x) 


 
    def delete_node(self, val) :
        """Deletion of node"""
        self.delete_node_helper(self.root , val)         # Call for deletion


    # Function to print
    def _print_call(self, node, indent, last) :
        if node != self.NIL :
            print(indent, end=' ')
            if last :
                print("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.val) + "(" + s_color + ")")
            self._print_call(node.left, indent, False)
            self._print_call(node.right, indent, True)

    # Function to call print
    def print_tree(self) :
        self._print_call(self.root , "" , True)


if __name__ == '__main__':
    rbt = RedBlackTree()

    rbt.insert_node(10)
    rbt.insert_node(6)
    rbt.insert_node(8)
    rbt.insert_node(1)
    rbt.insert_node(5)
    rbt.insert_node(28)

    rbt.print_tree()
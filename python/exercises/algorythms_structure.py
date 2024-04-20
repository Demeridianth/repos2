from collections import deque
import arotation_to_rightay as arotation_to_right
from arotation_to_rightay import *
from binarytree import Node
import zlib


#fizz_buzzpip
# def fizzbuzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0:
#             print('fizz', end='')
#         if i % 5 == 0:
#             print('buzz', end='')

#         print()


def fizz_buzz():
    for i in range(0, 101):
        print(i)
        if i % 5 == 0 and i % 3 == 0:
            print('fizz_buzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)
        
        
# fizz_buzz()






def bubbleSort(arotation_to_rightay):
    
  # loop to access each arotation_to_rightay element
  for i in range(len(arotation_to_rightay)):

    # loop to compare arotation_to_rightay elements
    for j in range(0, len(arotation_to_rightay) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if arotation_to_rightay[j] > arotation_to_rightay[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = arotation_to_rightay[j]
        arotation_to_rightay[j] = arotation_to_rightay[j+1]
        arotation_to_rightay[j+1] = temp


# data = [-2, 45, 0, 11, -9]
# bubbleSort(data)
# print('Sorted Arotation_to_rightay in Ascending Order:')
# print(data)



def bubble_sort(num_list):
    for i in range (len(num_list)- 1, 0, - 1):
        for j in range(i):
            if num_list[j] > num_list[j + 1]:
                temp = num_list[j]
                num_list[j] = num_list[j + 1]
                num_list[j + 1] = temp
# my_list = [4, 266, 9 , 24, 44, 54, 41, 89, 20]
# bubble_sort(my_list)
# print(my_list)
# [4, 9, 20, 24, 41, 44, 54, 89, 266]


##########


#sequental search

# O(n)

def sequential_search (number_list, number):
    # found = False
    for i in number_list:
        if i == number:
            return True
    return False
    #         found = True
    #         break
    # return found

# print(sequential_search(range(0, 100), 2))


#binary search

def binary_search (number_list, number):
    first = 0
    last = len(number_list)-1
    number_found = False
    while first <= last and not number_found:
        middle = (first + last)//2
        if number_list[middle] == number:
            number_found = True
        else :
            if number < number_list[middle]:
                last = middle - 1
            else :
                first = middle + 1
    return number_found

# print(binary_search([1,2,3,4,5,6], 2))




def binary_search(arotation_to_right, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arotation_to_right[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarotation_to_rightay
        elif arotation_to_right[mid] > x:
            return binary_search(arotation_to_right, low, mid - 1, x)
 
        # Else the element can only be present in right subarotation_to_rightay
        else:
            return binary_search(arotation_to_right, mid + 1, high, x)
 
    else:
        # Element is not present in the arotation_to_rightay
        return -1
 
# Test arotation_to_rightay
arotation_to_right = [2, 3, 4, 10, 40]
x = 3
 
# Function call
result = binary_search(arotation_to_right, 0, len(arotation_to_right)-1, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in arotation_to_rightay")



#recursion

#Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
# For example:
# Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

def add_digits(number):
    number = str(number)
    if len(number) == 1 :
        return int(number)
    the_sum = 0
    for c in number:
        the_sum += int(c)
        return add_digits(the_sum)
    
# print(add_digits(4444))

#############################################################################################



#Abstract Data Types
#STACKS


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return bool(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if self.items:
            return self.items[-1]
        return None
    
    def __len__(self):
        return len(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    

# Reverse with stack

my_string = 'String'
stack = Stack()

reversed_string = ''
for c in my_string:
    stack.push(c)

while not stack.is_empty():
    reversed_string += stack.pop()

# print(reversed_string)



def balanced_parenthesis(expression):
    stack = []
    for c in expression:
        if c == '(' :
            stack.append(c)
        elif c == ')':
            if len(stack) < 1 :
                return False
    
            stack.pop()
    if len(stack) == 0 :
        return True
    return False

# print(balanced_parenthesis('(())'))



#####################################################################################


#nodes

class Days:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next_data = None

day1 = Days('Mon')
day2 = Days('Tue')
day3 = Days('Wed')
day4 = Days('Thu')

day1.next_data = day2
day2.next_data = day3
day3.next_data = day4

node = day1
while node:
    # print(node.data)
    node = node.next_data




# LINKED LISTS




#single linked
#on top
class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        previous_head = self.head
        self.head = Node(data)
        self.head.next = previous_head


# linked_list = LinkedList()
# linked_list.add(1)
# linked_list.add(2)
# linked_list.add(3)

# node = linked_list.head
# while node:
#     print(node.data)
#     node = node.next







# methods

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, new_node):
        curotation_to_rightent = self.head
        if curotation_to_rightent:
            while curotation_to_rightent.next:
                curotation_to_rightent = curotation_to_rightent.next
            curotation_to_rightent.next = new_node
        else:
            self.head = new_node

    def delete(self, val):
        curotation_to_rightent = self.head
        if curotation_to_rightent.val == val:
            self.head = curotation_to_rightent.next
        else:
            while curotation_to_rightent:
                if curotation_to_rightent.val == val:
                    break
                previous = curotation_to_rightent
                curotation_to_rightent = curotation_to_rightent.next
            if curotation_to_rightent == None:
                return
            previous.next = curotation_to_rightent.next
            curotation_to_rightent = None 

    def insert(self, new_element, position):
        count = 1
        curotation_to_rightent = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while curotation_to_rightent:
            if count + 1 == position:
                new_element.next = curotation_to_rightent.next
                curotation_to_rightent.next = new_element
                return
            else:
                count += 1
                curotation_to_rightent = curotation_to_rightent.next

    # def print(self):
    #     curotation_to_rightent = self.head
    #     while curotation_to_rightent:
    #         print(curotation_to_rightent.val)
    #         curotation_to_rightent = curotation_to_rightent.next


e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e9 = Node(9)
linked_list = LinkedList(e1)
linked_list.append(e2)
linked_list.append(e3)
linked_list.append(e4)
linked_list.insert(e9, 3)
linked_list.delete(4)

# node = linked_list.head
# while node:
#     print(node.val)
#     node = node.next





# __repr__
# yield

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None 

    def __repr__(self):
        return self.data
    

class LinkedList:
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(data=element)
                node = node.next

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
    # inserting at the beginning
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # inserting at the end
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return None
        for curotation_to_rightent_node in self:
            pass
        curotation_to_rightent_node.next = node

    # inserting after an existing node
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('the list is empty')
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return 
        raise Exception(f'Node with data {target_node_data} not found')
    
    # inserting before an existing node
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('the list is empty')
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception(f'Node with data {target_node_data} not found')
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    #iterator generator
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

# lst = LinkedList(['b', 'c', 'd', 'e'])
# lst.add_last(Node('f'))
# lst.add_first(Node('a'))
# lst.add_after('b', Node('2'))
# lst.add_before('d', Node('z'))
# lst.remove_node('f')
# print(lst)

# lst = LinkedList()
# first_node = Node('a')
# lst.head = first_node
# second_node = Node('b')
# third_node = Node('c')
# first_node.next = second_node
# second_node.next = third_node

# for node in lst:
#     print(node)



# DOUBLY LINKED LIST
class Node:
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
        def __init__(self) -> None:
            self.head = None

        def check_if_empty(self):
            if self.head is None:
                return True
            return False
        
        def add_at_beginning(self, data):
            new_node = Node(data)
            if self.check_if_empty():
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node

        def add_at_end(self, data):
            new_node = Node(data)
            if self.check_if_empty():
                self.add_at_beginning(data)
            else:
                temp = self.head
                while temp.next: # to last node
                    temp = temp.next
                temp.next = new_node
                new_node.previous = temp

        def add_after_node(self, new_data, target_node_data):
            temp = self.head
            while temp:
                if temp.data == target_node_data:
                    break
                temp = temp.next
            if temp is None:
                print(f'{target_node_data} is not in the list')
            else:
                new_node = Node(new_data)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next = new_node

        def add_at_position(self, data, position):
            temp = self.head
            count = 0
            while temp:
                if count == position - 1:
                    break
                count += 1
                temp = temp.next
            if position == 1:
                self.add_at_beginning(data)
            elif temp is None:
                print(f'there are less then {position - 1} elements')
            elif temp.next is None:
                self.add_at_end(data)
            else:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.prev = temp
                temp.next.prev = new_node
                temp.next

        def delete(self, val):
            if self.check_if_empty():
                print("Linked List is empty. Cannot delete elements.")
            elif self.head.next is None:
                if self.head.data == val:
                    self.head = None
            else:
                temp = self.head
                while temp is not None:
                    if temp.data == val:
                        break
                    temp = temp.next
                if temp is None:
                    print("Element not present in linked list. Cannot delete element.")
                else:
                    temp.next = temp.previous.next
                    temp.next.previous = temp.previous
                    temp.next = None
                    temp.previous = None



linked_list = DoublyLinkedList()
# print(linked_list.check_if_empty())
linked_list.add_at_beginning(1)
linked_list.add_at_end(2)
head = linked_list.head
while head:
    # print(head.data)
    head = head.next






# doubly linked list
# with 'tail'

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None

        else:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None


    def add_last(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail

        if self.tail == None:
            self.head = new_node
            self.tail = new_node
            new_node.next = None
        
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node


    def pop_first(self):  # remove and return first node
        if self.head == None:
            print('list is empty')
        else:
            temp = self.head
            temp.next.prev = None # remove previous pointer referotation_to_righting to old head
            self.head = temp.next # make second element the new head
            temp.next = None # remove next pointer referotation_to_righting to new head
            return temp.data
        
    def pop_last(self):
        if self.tail == None:
            print('list is empty')
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = temp.prev
            temp.prev = None
            return temp.data


linked_list = LinkedList()
linked_list.add_first(Node('1'))
linked_list.add_first(Node('2'))
linked_list.add_last(Node('3'))
node = linked_list.head
# while node:
#     print(node.data)
#     node = node.next




# collections.deque
# from collections import deque

deque(['a','b','c'])
#deque(['a', 'b', 'c'])

deque('abc')
#deque(['a', 'b', 'c'])

deque([{'data': 'a'}, {'data': 'b'}])
#deque([{'data': 'a'}, {'data': 'b'}])

llist = deque("abcde")
# print(llist)
#deque(['a', 'b', 'c', 'd', 'e'])

llist.appendleft("z")
#print(llist)
#deque(['z', 'a', 'b', 'c', 'd', 'e'])


# queue:
queue = deque()

queue.append('Mon')
queue.append('Tue')
queue.append('Wed')
queue.popleft()
# print(queue)


#stack
stack = deque()

stack.appendleft('Mon')
stack.appendleft('Tue')
stack.appendleft('Wed')
stack.popleft()
# print(stack)






# ARRAYS  /  МАССИВЫ
from array import array

#  TYPECODE	C TYPE	            PYTHON TYPE	      SIZE
# 'b'	    signed char	        int	                1
# 'B'	    unsigned char	    int	                1
# 'u'	    wchar_t	            Unicode character	2
# 'h'	    signed short	    int	                2
# 'H'	    unsigned short	    int	                2
# 'i'	    signed int	        int	                2
# 'I'	    unsigned int	    int	                2
# 'l'	    signed long	        int	                4
# 'L'	    unsigned long	    int	                4
# 'q'	    signed long long	int	                8
# 'Q'	    unsigned long long	int	                8
# 'f'	    float	            float	            4
# 'd'	    double	            float	            8

numbers =  array('i', [1, 2, 3])
numbers_float = array('d',[10.0,20.0,30.0])
# print(numbers_float)

ar = array('i', [1, 2, 3])
# print('the new arotation_to_rightay is : ', end=' ')
# for i in range(0, 3):
#     print(ar[i], end=' ')
# print()








# BINARY TREES

# binary tree

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
#          10
#        /    \
#       34      89
#     /    \  /    \
#  20     45  2    54

# print
# root.traverse_in_order(root)


#          10
#        /    \
#       34      89
#     /    \  /    \
#  20     45  2    54


# 2 10 20 34 45 54 89






# binary search tree / faster / O(logN)
# methods use recursion

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

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

# In order traversal through TREE
# LEFT -> ROOT -> RIGHT
    def traverse_in_order(self, root):
        result = []
        if root:
            result = self.traverse_in_order(root.left)
            result.append(root.data)
            result = result + self.traverse_in_order(root.right)
        return result
    
# pre order traversal
# root -> Left -> Right
    def traverse_pre_order(self, root):
        result = []
        if root:
            result.append(root.data)
            result = result + self.traverse_pre_order(root.left)
            result = result + self.traverse_pre_order(root.right)
        return result
    
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

# root = Node(27)
# root.insert(6)
# root.insert(14)
# root.insert(3)
# root.insert(35)
# root.insert(28)
# root.insert(2)
# root.insert(42)
# root.insert(3)
# root.print_tree()
# print(root.search(1))
# print(root.traverse_in_order(root))
# print(root.traverse_pre_order(root))


# test
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

    def insert(self, value):
        if self.value:
            if self.value > value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif self.value < value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value


        



# MODULE Binarytree



# HASH TABLES O(1)
# Хеширование — операция, которая преобразует любые входные данные в строку или число фиксированной длины. Функция, реализующая алгоритм преобразования, называется «хеш-функцией». При этом результат хеширования называют «хешем» или «хеш-суммой».

# Другими словами, в хэш-таблице хранятся пары ключ-значение, но ключ генерируется с помощью функции хеширования.
# Для этого хеш-таблица использует индексированный массив и функцию для хеширования ключей.

# Ruby — Hash
# Lua — Table
# JavaScript — Object
# Elixir/Java — Map


# HASH TO INDEX

# import zlib =>  crc32 hash algorythm
# Этот алгоритм удобен для наглядности

# data = b'Algoryth'  # => byte string
# hash = zlib.crc32(data)
# # print(hash) => 1354533541

# index = abs(hash) % 1000
# print(index)  => 541



# HASHING FROM INSIDE

data = {}
internal_arotation_to_rightay = []
data['key'] = 'val'
#        ||
#        \/
hash = zlib.crc32(b'key')
index = abs(hash) % 1000
internal_arotation_to_rightay[index] = ['key', 'val']




class HashTable:
    def __init__(self) -> None:
        self.list = [None] * 11

    @staticmethod
    def hash(number):
        return number % 11
    
    def set(self, number, val):
        self.list[self.hash(number)] = val

    def get(self, number):
        return self.list[hash(number)]


hash_table = HashTable()
hash_table.set(1, 'ALGO')
hash_table.set(5, 'RHYTM')
# print(hash_table.get(1))
# print(hash_table.get(5))




# RED, BLACK TREE     





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
        if y.left != self.NULL :
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
        if y.right != self.NULL :
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
        z = self.NULL
        while node != self.NULL :                          # Search for the node having that value/ key and store it in 'z'
            if node.val == key :
                z = node

            if node.val <= key :
                node = node.right
            else :
                node = node.left

        if z == self.NULL :                                # If Kwy is not present then deletion not possible so return
            print("Value not present in Tree !!")
            return

        y = z
        y_original_color = y.color                          # Store the color of z- node
        if z.left == self.NULL :                            # If left child of z is NULL
            x = z.right                                     # Assign right child of z to x
            self.__rb_transplant(z ,z.right)            # Transplant Node to be deleted with x
        elif (z.right == self.NULL) :                       # If right child of z is NULL
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
        if node != self.NULL :
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









            
                
        





        










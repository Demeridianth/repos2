from collections import deque
import array as arr
from array import *
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






def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


# data = [-2, 45, 0, 11, -9]
# bubbleSort(data)
# print('Sorted Array in Ascending Order:')
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




def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
arr = [2, 3, 4, 10, 40]
x = 3
 
# Function call
result = binary_search(arr, 0, len(arr)-1, x)
 
# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")



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
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                previous = current
                current = current.next
            if current == None:
                return
            previous.next = current.next
            current = None 

    def insert(self, new_element, position):
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next

    # def print(self):
    #     current = self.head
    #     while current:
    #         print(current.value)
    #         current = current.next


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
#     print(node.value)
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
        for current_node in self:
            pass
        current_node.next = node

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

        def delete(self, value):
            if self.check_if_empty():
                print("Linked List is empty. Cannot delete elements.")
            elif self.head.next is None:
                if self.head.data == value:
                    self.head = None
            else:
                temp = self.head
                while temp is not None:
                    if temp.data == value:
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
            temp.next.prev = None # remove previous pointer referring to old head
            self.head = temp.next # make second element the new head
            temp.next = None # remove next pointer referring to new head
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
# import array as arr
# from array import *

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
# print('the new array is : ', end=' ')
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
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        pass


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

data = b'Algoryth'  # => byte string
hash = zlib.crc32(data)
# print(hash) => 1354533541

index = abs(hash) % 1000
# print(index)  => 541



# HASHING FROM INSIDE

data = {}
internal_array = []
data['key'] = 'value'
#        ||
#        \/
hash = zlib.crc32(b'key')
index = abs(hash) % 1000
internal_array[index] = ['key', 'value']




class HashTable:
    def __init__(self) -> None:
        self.list = [None] * 11

    @staticmethod
    def hash(number):
        return number % 11
    
    def set(self, number, value):
        self.list[self.hash(number)] = value

    def get(self, number):
        return self.list[hash(number)]


hash_table = HashTable()
hash_table.set(1, 'ALGO')
hash_table.set(5, 'RHYTM')
# print(hash_table.get(1))
# print(hash_table.get(5))






                    


    















            
                
        





        










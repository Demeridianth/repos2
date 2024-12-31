# 1. Constant Time: O(1)
# Description: The algorithm's running time does not depend on the input size.
# Example: Accessing an element in an array by index.
# Visualization: The running time remains flat, no matter how large the input size gets.

def get_first_element(arr):
    if not arr:
        return None  # Handle empty array
    return arr[0]  # Access the first element of the array



# 2. Logarithmic Time: O(log n)
# Description: The algorithm's running time grows logarithmically with the input size. It typically occurs in divide-and-conquer algorithms.
# Example: Binary search.
# Visualization: The running time increases slowly as the input size grows.

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if arr[mid] == target:  # Target found
            return mid
        elif arr[mid] < target:  # Target is in the right half
            left = mid + 1
        else:  # Target is in the left half
            right = mid - 1
    
    return -1  # Target not found



# 3. Linear Time: O(n)
# Description: The running time grows linearly with the size of the input.
# Example: Traversing all elements in an array.
# Visualization: The running time grows proportionally to the input size.

def find_max(arr):
    if not arr:
        return None  # Handle empty array

    max_value = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > max_value:
            max_value = num  # Update max_value if a larger number is found
    
    return max_value



# 5. Quadratic Time: O(n^2)
 
# Description: The running time grows quadratically with the input size. This is common in algorithms with nested loops.
# Example: Bubble sort, selection sort.
# Visualization: The running time increases sharply with input size.

def find_all_pairs(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            pairs.append((arr[i], arr[j]))  # Pair each element with every other element
    return pairs
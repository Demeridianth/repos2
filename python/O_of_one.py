def check_membership(data, key):
    return data.get(key, "Key not found")  # Checking if a key exists

# Example usage
data = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}
key = "Bob"
result = check_membership(data, key)
print(result)  # Output: 30
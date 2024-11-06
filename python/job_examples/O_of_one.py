def check_membership(data, key):
    return data.get(key, "Key not found")  # Checking if a key exists

# Example usage
data = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}


def main() -> None:
    key = "Bob"
    result = check_membership(data, key)
    print(result)  # Output: 30

if __name__ == '__main__':
    main()
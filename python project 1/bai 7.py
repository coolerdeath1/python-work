def count_chars(filename):
    char_counts = {}
    with open(filename, 'r') as f:
        text = f.read()
        for char in text:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    for char, count in char_counts.items():
        print(f"{char}: {count}")

# Example usage
count_chars('example.txt')
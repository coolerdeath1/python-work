text = "Write a Python program that prints long text, converts it to a list, and prints all the words and the frequency of each word."
print(text)

words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print(key, value)
#Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other. 
def all_unique(numbers):
    return len(numbers) == len(set(numbers))
    
numbers = [1, 2, 3, 4]
result = all_unique(numbers)
print(result)
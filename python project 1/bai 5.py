digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(digits)):
    for j in range(i+1, len(digits)):
        for k in range(j+1, len(digits)):
            print(digits[i], digits[j], digits[k])
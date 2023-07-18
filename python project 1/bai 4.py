def find_triplets(arr):
    n = len(arr)
    found = False
    result = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    result.append([arr[i], arr[j], arr[k]])
                    found = True
    if not found:
        return "No triplets found"
    else:
        return result

arr = [0, -1, 2, -3, 1]
print(find_triplets(arr))
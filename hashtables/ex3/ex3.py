def intersection(arrays):
    numbers = {'cross': []}
    k = len(arrays)
    n = 0
    for i in range(k):
        if len(arrays[i]) > n:
            n = len(arrays[i])
    for i in range(n):
        for j in range(k):
            if i > len(arrays[j]) - 1:
                continue
            num = arrays[j][i]
            if num in numbers:
                numbers[num] += 1
                if numbers[num] == k:
                    numbers['cross'].append(num)
            else:
                numbers[num] = 1
    return numbers['cross']


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

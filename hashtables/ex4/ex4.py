def has_negatives(a):
    results = []
    cache = {}
    for num in a:
        if num < 0:
            neg_num = num * -1
            if neg_num in cache:
                results.append(neg_num)
            else:
                cache[neg_num] = 1
        else:
            if num in cache:
                results.append(num)
            else:
                cache[num] = 1
    return results


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

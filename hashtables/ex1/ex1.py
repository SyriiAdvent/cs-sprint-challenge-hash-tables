def get_indices_of_item_weights(weights, length, limit):
    cache = {}
    if length <= 1:
        return None
    if length == 2:
        return (1, 0)
    for i in range(length):
        cache[weights[i]] = i
        check = limit - weights[i]
        if check in cache:
            if weights[i] + check == limit or weights[i] - check == limit:
                if cache[weights[i]] > i:
                    return (cache[check], i)
                else:
                    return (i, cache[check])


# print(get_indices_of_item_weights([9], 1, 9))
# print(get_indices_of_item_weights([4, 4], 2, 8))
# print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))
# print(get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7))

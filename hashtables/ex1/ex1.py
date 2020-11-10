def get_indices_of_item_weights(weights, length, limit):
    hash_table = {}

    for i in range(length):
        bucket = []
        cur_weight = weights[i]
        value = hash_table.get(limit-cur_weight)

        if value is None:
            hash_table[cur_weight] = i
        else:
            if value > i:
                bucket.append(value)
                bucker.append(i)
            else:
                bucket.append(i)
                bucket.append(value)
            return bucket

    return None


print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21))

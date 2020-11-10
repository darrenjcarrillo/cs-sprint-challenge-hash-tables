def intersection(arrays):
    elements = {}
    result = []

    for arr in arrays:
        for each_element in arr:
            if each_element in elements:
                elements[each_element] += 1
            else:
                elements[each_element] = 1

            if elements[each_element] == len(arrays):
                result.append(each_element)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

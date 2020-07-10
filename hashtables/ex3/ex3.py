def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    len = 0
    result = []
    for array in arrays:
        len +=1
        for num in array:
            if num not in cache:
                cache[num] = 1
            else:
                cache[num] += 1
                if cache[num] == len and num not in result:
                    result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

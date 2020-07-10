def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    #adds all number to cache
    for num in a:
        cache[num] = 1
        #if current's inverse is in cache,
        # add positive to list, no 0
        if num != 0 and -num in cache:
            result.append(abs(num))

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

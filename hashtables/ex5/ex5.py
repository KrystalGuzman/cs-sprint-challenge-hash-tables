# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    cache = {}

    # stores queries in cache
    for x in queries:
        cache[x] = x
    
    for f in files:
        #file name is last part
        words = f.split("/")
        if words[-1] in cache:
            #adds to result
            result.append(f)

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))

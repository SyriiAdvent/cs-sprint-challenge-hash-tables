def finder(files, queries):
    result = []
    paths = {}

    for path in files:
        index = len(path) - 1
        char = path[index]
        key = ''

        while char != '/':
            key = char + key
            index -= 1
            char = path[index]

        index = index + 1
        if key in paths:
            paths[key].append(path[:index])
        else:
            paths[key] = [path[:index]]

    for q in queries:
        if q in paths:
            for i in range(len(paths[q])):
                result.append(f'{paths[q][i]}{q}')
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

def garbage_collector(array):
    for x in range(0, len(array)):
        array[x].append(None)
    return array

def trasnpose(arr):
    return list(map(list, zip(*arr)))

def rotate(arr):
    # rotate the array 90 degrees clockwise.
    return list(map(list, zip(*arr[::-1])))


if __name__ == '__main__':
    arr = [[1, 1, 1], [2, 2, 2]]
    print(rotate(arr))
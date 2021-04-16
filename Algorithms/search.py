
# 선형 탐색
def linear_search(arr, key):
    for idx, val in enumerate(arr):
        if val == key:
            return idx
    return -1



# 이진 탐색
def binary_search(arr, key):
    # arr.sort()
    l, r = 0, len(arr)-1
    while r >= l:
        c = (l + r) // 2
        if arr[c] == key:
            return c
        elif arr[c] > key:
            r = c - 1
        else:
            l = c + 1


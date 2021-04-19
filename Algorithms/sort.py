

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        exchange = 0
        for j in range(n-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                exchange += 1
        
        if exchange == 0:
            break
    return arr


def cocktail_shaker_sort(arr):
    left, right = 0, len(arr)-1
    last = right

    while left < right:
        for i in range(right, left, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                last = i
        left = last

        for i in range(left, right):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                last = i
        right = last

    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

if __name__ == '__main__':
    print(insertion_sort([1, 0, 4, 2, 7]))
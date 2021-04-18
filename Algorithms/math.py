
def median(arr):
    arr = sorted(arr)
    mid, rmn = divmod(len(arr), 2)
    if rmn == 0:
        return (arr[mid-1] + arr[mid]) * 0.5
    else:
        return arr[mid]


def factorial(n):
    if n < 0:
        return "Input non-negative int"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)



if __name__ == '__main__':
    print(greatest_common_divisor(35, 5))
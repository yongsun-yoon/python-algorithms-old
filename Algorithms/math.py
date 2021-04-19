
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


def least_common_multiple(a, b):
    return a * b // greatest_common_divisor(a, b)


# 10진수를 base 진수로 변경
def numeral_system(num, base):
    notation = '0123456789ABCDEF'
    q, r = divmod(num, base)
    n = notation[r]
    return numeral_system(q, base) + n if q else n


def prime_factorization(num):
    ret = []
    p = 2

    while p <= num:
        if num % p == 0:
            ret.append(p)
            num /= p
        else:
            p += 1
    return ret


if __name__ == '__main__':
    print(prime_factorization(12))
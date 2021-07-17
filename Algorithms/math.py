
def median(arr:list) -> float:
    """중앙값 계산"""
    arr = sorted(arr)
    mid, rmn = divmod(len(arr), 2)
    if rmn == 0:
        return (arr[mid-1] + arr[mid]) * 0.5
    else:
        return arr[mid]


def factorial(n:int) -> int:
    """팩토리얼 계산"""
    if n < 0:
        return "Input non-negative int"
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)


def greatest_common_divisor(a:int, b:int) -> int:
    """최대공약수 계산"""
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def least_common_multiple(a:int, b:int) -> int:
    """최소공배수 계산"""
    return a * b // greatest_common_divisor(a, b)


def numeral_system(num:int, base:int, prefix:bool) -> str:
    """10진수를 2, 8, 16진수로 변경"""
    if base == 2:
        return f'{num:#b}' if prefix else f'{num:b}'
    elif base == 8:
        return f'{num:#o}' if prefix else f'{num:o}'
    elif base == 16:
        return f'{num:#x}' if prefix else f'{num:x}'

    
def general_numeral_system(num:int, base:int) -> str:
    """10진수를 base진수로 변경"""
    notation = '0123456789ABCDEF'
    q, r = divmod(num, base)
    n = notation[r]
    return numeral_system(q, base) + n if q else n


def inverse_numeral_system(num:str, base:int) -> int:
    """2, 8, 16진수를 10진수로 변경"""
    return int(num, base)
    

def prime_factorization(num:int) -> list:
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

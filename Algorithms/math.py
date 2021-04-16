
# 중앙값 구하기
def median(arr):
    arr = sorted(arr)
    mid, rmn = divmod(len(arr), 2)
    if rmn == 0:
        return (arr[mid-1] + arr[mid]) * 0.5
    else:
        return arr[mid]



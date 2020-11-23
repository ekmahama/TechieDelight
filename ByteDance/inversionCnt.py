from collections import defaultdict


def inversionCnt(arr):
    """Naive Solution"""
    ret = 0
    for i in range(len(arr)-1):
        for j in range(1, len(arr)):
            if i < j and arr[i] > arr[j]:
                ret += 1
    return ret


def inversionCnt_v1(arr):
    """Divide and Conquer"""


arr = [1, 9, 6, 4, 5]
print(inversionCnt(arr))


defaultdict()

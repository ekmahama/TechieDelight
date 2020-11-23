def mergeSort(arr, aux, left, right):
    if left >= right:
        return
    mid = (left + right)//2
    mergeSort(arr, aux, left, mid)
    mergeSort(arr, aux, mid+1, right)
    merge(arr, aux, left, mid, right)


def merge(arr, aux, left, mid, right):
    i = left  # begin index for left array
    j = mid+1  # begin index for right array
    k = left  # index for copying into aux array

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            aux[k] = arr[i]
            i += 1
        else:
            aux[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        aux[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        aux[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right+1):
        arr[i] = aux[i]


if __name__ == "__main__":
    arr = [1, 4, 6, 1, 2, 4, 3, 0]
    left = 0
    right = len(arr)-1
    aux = [0, ]*(right+1)
    mergeSort(arr, aux, left, right)
    print(arr)

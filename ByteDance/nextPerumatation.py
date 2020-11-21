def nextPermutation(arr):
    if len(arr) == 1:
        return arr
    # Find the largest index i such that arr[i-1]<arr[i]
    # If i is not the first index:
    #   find index j to the right of i such that arr[j]>arr[i-1]
    #   swap arr[j]>arr[i-1]
    #   sort subarry arr[i:]

    def swap(i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    i = len(arr)-1
    while arr[i-1] >= arr[i]:
        i -= 1
        if i == 0:
            return sorted(arr)
    j = len(arr)-1

    while j > i and arr[j] <= arr[i-1]:
        j -= 1
    swap(i-1, j)
    arr[i:] = sorted(arr[i])
    return arr


if __name__ == '__main__':
    arr = ['1', '2', '3']
    nextPermutation(arr)

def frogJump(stones):
    for i in range(3, len(stones)):
        if stones[i] > stones[i-1]*2:
            return False

    stack = []
    stack.append((0, 0))

    while stack:
        curPos, prevJump = stack.pop()

        for j in range(prevJump-1, prevJump+2):
            if j <= 0:
                continue
            nextPost = curPos + j

            if nextPost == stones[-1]:
                return True
            if nextPost in stones:
                stack.append((nextPost, j))
    return False


arr = [0, 1, 3, 5, 6, 8, 12, 17]
# arr = [0, 1, 2, 3, 4, 8, 9, 11]
# arr=[0,2]
res = frogJump(arr)
print(res)

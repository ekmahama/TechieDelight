from collections import defaultdict


def maxSquare(M):
    if not M or not M[0]:
        return
    R = len(M)
    C = len(M[0])

    maxSize = 0

    memo = defaultdict(int)

    for i in range(R):
        for j in range(C):
            if i > 0 and j > 0 and M[i][j] == 1:
                memo[(i, j)] = min(memo[(i, j-1)],
                                   memo[(i-1, j)], memo[(i-1, j-1)])+1
            else:
                memo[(i, j)] = M[i][j]

            maxSize = max(memo[(i, j)], maxSize)
    return maxSize


M = [
    [0, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1]
]

res = maxSquare(M)

"""
Longest Common Subsequence Problem
"""


from collections import defaultdict


def LCS_v1(seq1, seq2):
    """
    Using optimal substructure with no memoization
    """
    if len(seq1) == 0 or len(seq2) == 0:
        return 0
    if seq1[-1] == seq2[-1]:
        return LCS_v1(seq1[:-1], seq2[-1]) + 1

    return max(LCS_v1(seq1, seq2[:-1]), LCS_v1(seq1[:-1], seq2))


def LCS_v2(seq1, seq2, memo={}):
    """
    Using optimal substructure with no memoization
    """
    if len(seq1) == 0 or len(seq2) == 0:
        return 0

    key = (seq1, seq2)

    if key not in memo:
        if seq1[-1] == seq2[-1]:
            memo[key] = LCS_v2(seq1[:-1], seq2[:-1]) + 1

        else:
            memo[key] = max(LCS_v2(seq1, seq2[:-1]), LCS_v2(seq1[:-1], seq2))

    return memo[key]


def LCS_v3(seq1, seq2, memo={}):
    """
    Using optimal substructure with no memoization
    """
    if len(seq1) == 0 or len(seq2) == 0:
        return " "

    key = (seq1, seq2)

    if key not in memo:
        if seq1[-1] == seq2[-1]:
            memo[key] = LCS_v3(seq1[:-1], seq2[:-1]) + seq1[-1]

        else:
            sub1 = LCS_v3(seq1, seq2[:-1])
            sub2 = LCS_v3(seq1[:-1], seq2)

            if len(sub1) > len(sub2):
                memo[key] = sub1
            else:
                memo[key] = sub2

    return memo[key]


"""
Longest Common Subsequence Problem
"""


def LCS_v4(seq1, seq2):
    """
    Bottom up approach
    """
    memo = defaultdict(int)
    m = len(seq1)
    n = len(seq2)

    for i in range(1, m + 1):
        for j in range(1, n+1):
            if seq1[i-1] == seq2[j-1]:
                memo[(i, j)] = memo[(i-1, j-1)] + 1
            else:
                memo[(i, j)] = max(memo[(i, j-1)], memo[(i-1, j)])

    return memo[(m, n)]


seq1 = "ABCD"
seq2 = "CABC"
LCS_v2(seq1, seq2)

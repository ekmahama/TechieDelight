def fibbo(n):
    """Naive Solution"""
    if n <= 1:
        return n
    return fibbo(n-2) + fibbo(n-1)


def fibbo_v2(n, memo={}):
    """Dynamic Programming"""
    if n <= 1:
        return n
    memo[n] = fibbo_v2(n-2, memo) + fibbo_v2(n-1, memo)
    return memo[n]


print(fibbo(10))
print(fibbo(10))

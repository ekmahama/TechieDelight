def helper(str1, str2, m={}):
    if str1 == str2:
        return True
    for i in range(len(str1)):
        if str1[i] not in m:
            m[str1[i]] = str2[i]
        elif m[str1[i]] != str2[i]:
            return False
    return len(set(str2)) < 26


def findMinOps(str1, str2):
    m = {}
    if not helper(str1, str2, m):
        return -1
    # check for cycles
    if set(m.values()) == set(m.keys()):
        return 2*len(m.keys()) - 2

    # check for common items in both strs
    else:
        res = len(m)
        for key, val in m.items():
            if key == val:
                res -= 1
    return res


# s1 = 'ababcc'
# s2 ='cccccc'
# s1 = 'aaa'
# s2 ='bbb'
# s1='abcd'
# s2='bead'
s1 = 'ab'
s2 = 'ba'
findMinOps(s1, s2)

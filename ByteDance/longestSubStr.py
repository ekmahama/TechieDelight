def longestSubStr(s):
    """
    Find longest substring with no repeating characters
    """
    left = right = 0
    maxLen = 0
    maxSubStr = []

    while right < len(s):
        char = s[right]
        if char not in maxSubStr:
            maxSubStr.append(char)

            if len(maxSubStr) > maxLen:
                ret = maxSubStr.copy()
                maxLen = len(ret)
            right += 1
        else:
            maxSubStr.remove(s[left])
            left += 1
    return ''.join(ret)


s = "abbcdafeegh"
res = longestSubStr(s)

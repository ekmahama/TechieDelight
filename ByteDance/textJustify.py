def justify(arr, width):
    res = []
    endlag = False
    string = []
    cntwithSpace = 0  # with space
    cntwintoutSpace = 0  # without space
    while arr:
        word = arr.pop(0)
        if (cntwithSpace+len(word)) <= width:
            cntwintoutSpace += len(word)
            cntwithSpace += (len(word) + 1)
            string.append(word)
        else:
            if len(string) > 1:
                quot, rem = divmod((width-cntwintoutSpace), len(string)-1)

            else:
                quot = width-cntwintoutSpace
                rem = 0

            res.append(helper(string, quot, rem, endlag))

            string, cntwithSpace, cntwintoutSpace = [], 0, 0
            arr = [word, ] + arr

    endlag = True
    if len(string) > 1:
        quot, rem = divmod((width-cntwintoutSpace), len(string)-1)
    else:
        quot = width-cntwintoutSpace
        rem = 0

    res.append(helper(string, quot, rem, endlag))

    return res


def helper(string, quot, rem, endlag=False):
    res = ''
    # endline case with one word
    if len(string) == 1 and endlag:
        res = string[0] + ' '*quot

    # endline case with more than one word
    elif len(string) > 1 and endlag:
        for i, w in enumerate(string):
            if i < len(string)-1:
                res = res + w + ' '
                rem -= 1
            else:
                res = res + w + ' '*quot

    # Not endline case with one word
    if len(string) == 1 and not endlag:
        res = res + string[0] + ' '*rem

    # Not endline case with more than one word and rem = 0
    elif len(string) > 1 and rem == 0:
        for i, w in enumerate(string):
            if i < len(string)-1:
                res = res + w + ' '*(quot)
            else:
                res = res + w

    # Not endline case with more than one word and rem > 0
    elif len(string) > 1 and rem > 0:
        while rem:
            for i, w in enumerate(string):
                if i < len(string)-1 and rem > 0:
                    res = res + w + ' '*(quot+1)
                    rem -= 1
                elif i < len(string)-1 and rem <= 0:
                    res = res + w + ' '*(quot)
                else:
                    res = res + w
    return res


arr1 = ["This", "is", "an", "example", "of", "text", "justification."]
arr2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
arr3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to",
        "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]

examp = [(arr1, 16), (arr2, 16), (arr3, 20)]
for arr, width in examp:
    res1 = justify(arr, width)
    for line in res1:
        print(line, end=' ')
        print(len(line))
    print('####################################################')

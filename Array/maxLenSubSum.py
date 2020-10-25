import collections
import unittest


def maxLenSubSum(arr, s):
    """Naive Solution : Complext is O(N^3) since it takes O(N) to search n^2 subarrays"""
    subArrayList = collections.defaultdict(list)
    subArrayList[s].append(-1)
    ret = []
    for k in range(len(arr)):
        sum = 0
        for i in range(k, len(arr)):
            sum += arr[i]

            if sum in subArrayList and sum == s:
                for j in subArrayList[sum]:
                    ret.append(arr[j+1+k:i+1])
            else:
                subArrayList[sum].append(i)

    res = ret[0]
    for lst in ret[1:]:
        if len(lst) > len(res):
            res = lst
    return res


def maxLenSubSumV2(arr, s):
    dict = {}
    sum = 0
    dict[sum] = -1
    end_index = -1
    length = 0

    for i, val in enumerate(arr):
        sum += val

        if sum not in dict:
            dict[sum] = i

        if (sum - s) in dict and length < i - dict[sum-s]:
            length = i - dict[sum-s]
            end_index = i
    return arr[end_index - length + 1:end_index+1]


def maxLenSubSumV1(arr, s):
    pass


class Test(unittest.TestCase):
    def setUp(self):
        self.arr = [8, 5, 6, -5, 5, 3, 5, 3, -2, 0]
        self.s = 8

    def tearDown(self):
        pass

    def test_maxLenSubSum(self):
        self.assertEqual(maxLenSubSum(self.arr, self.s), [-5, 5, 3, 5])

    def test_maxLenSubSumV2(self):
        self.assertEqual(maxLenSubSumV2(self.arr, self.s), [-5, 5, 3, 5])


if __name__ == "__main__":
    unittest.main()

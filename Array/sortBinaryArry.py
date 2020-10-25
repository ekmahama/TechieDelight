import collections
import unittest


class Solution:
    def sortBinaryArrV1(self, arr):
        numZero = arr.count(0)
        n = len(arr)

        arr = [1, ] * n
        for i in range(numZero):
            arr[i] = 0
        return arr

    def sortBinaryArrV2(self, arr):
        count = collections.Counter(arr)
        ret = [0, ]*count[0] + [1, ]*count[1]
        return ret

    def sortBinaryArrV3(self, arr):
        pass


class Test(unittest.TestCase):
    def setUp(self):
        self.arr = [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]

    def tearDown(self):
        pass

    def test_sortBinaryArrV1(self):
        examp = Solution().sortBinaryArrV1(self.arr)
        self.assertTrue(examp == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    def test_sortBinaryArrV2(self):
        examp = Solution().sortBinaryArrV2(self.arr)
        self.assertTrue(examp == [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()

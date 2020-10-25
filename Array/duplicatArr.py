import collections
import unittest


class Solution:
    def duplicateEle(self, arr):
        res = collections.Counter(arr)

        return max(res, key=res.get)

    def duplicateEleV2(self, arr):
        xor = 0
        for i in arr:
            xor ^= i
        for j in range(1, len(arr)):
            xor ^= j

        return xor


class Test(unittest.TestCase):
    def setUp(self):
        self.arr = [1, 2, 3, 4, 2]
        self.arr1 = [1, 1, 2, 3, 4, 5]
        self.arr2 = [1, 2, 3, 3, 4, 5]
        self.arr3 = [1, 2, 3, 4, 5, 6, 6]

    def tearDown(self):
        pass

    def test_duplicateEle(self):
        examp = Solution().duplicateEle(self.arr)
        self.assertEqual(examp, 2)

        examp1 = Solution().duplicateEle(self.arr1)
        self.assertEqual(examp1, 1)

        examp2 = Solution().duplicateEle(self.arr2)
        self.assertEqual(examp2, 3)

        examp3 = Solution().duplicateEle(self.arr3)
        self.assertEqual(examp3, 6)

    def test_duplicateEleV2(self):
        examp = Solution().duplicateEleV2(self.arr)
        self.assertEqual(examp, 2)

        examp1 = Solution().duplicateEleV2(self.arr1)
        self.assertEqual(examp1, 1)

        examp2 = Solution().duplicateEleV2(self.arr2)
        self.assertEqual(examp2, 3)

        examp3 = Solution().duplicateEleV2(self.arr3)
        self.assertEqual(examp3, 6)


# arr = [1, 2, 3, 4, 2]
# examp = Solution().duplicateEle(arr)

# print(examp)
if __name__ == '__main__':
    unittest.main()

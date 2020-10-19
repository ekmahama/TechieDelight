import unittest
import collections


def twoSum(arr, target):
    seen = {}
    for i, val in enumerate(arr):
        other = target - val

        if other in seen:
            return [seen[other], i]
        else:
            seen[val] = i
    return []


def threeSum(arr, target):
    valDict = {}
    for i, val in enumerate(arr):
        valDict[val] = i

    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            val = target - (arr[i] + arr[j])
            if val in valDict:
                if valDict[val] != i and valDict[val] != j:
                    return [valDict[val], i, j]
    return []


def quanTuple(arr, target):
    pairDict = collections.defaultdict(list)
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            val = target - arr[i]+arr[j]

            if val in pairDict:
                for pair in pairDict[val]:
                    x, y = pair
                    if (x != i and x != j) and (y != i and y != j):
                        return [i, j, pairDict[val][0][0], pairDict[val][0][1]]

            pairDict[arr[i]+arr[j]].append((i, j))
    return []

    # Testing for sample test cases


class testArraySum(unittest.TestCase):

    def setUp(self):
        self.arr = [2, 1, 9, 11, 23, -1, 7]
        self.target = 9

        self.arr1 = [2, 8, 4, 0, 9, 5, 6, 3]
        self.target1 = 6

        self.arr2 = [2, 8, 4, 0, 9, 5, 6, 3]
        self.target2 = 18

    def tearDown(self):
        pass

    def test_twoSum(self):
        self.assertEqual(twoSum(self.arr, self.target), [0, 6])

        self.arr = [2, 11, 9, 10, 23, -1, 7]
        self.target = 9

        self.assertEqual(twoSum(self.arr, self.target), [3, 5])

    def test_threeSum(self):
        self.assertEqual(threeSum(self.arr1, self.target1), [3, 0, 2])

    def test_quanTuple(self):
        self.assertEqual(quanTuple(self.arr2, self.target2), [2, 3, 1, 6])


if __name__ == "__main__":
    unittest.main()

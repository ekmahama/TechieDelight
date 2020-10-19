import unittest
import collections


class zeroSumSubArray:
    def __init__(self, arr):
        self.arr = arr

    def checkZeroSum(self):
        seen = set()

        # Take care of if subarry of first element is zero
        seen.add(0)
        sum = 0
        for val in self.arr:
            sum += val
            if sum in seen:
                return True
        return False

    def zeroSumList(self):
        subDict = collections.defaultdict(list)
        ret = []
        # Take care of if subarry of first element is zero
        subDict[0].append(-1)
        sum = 0
        for i in range(len(self.arr)):
            sum += self.arr[i]
            if sum in subDict:
                for j in subDict[sum]:
                    ret.append(self.arr[j+1:i+1])
            else:
                subDict[sum].append(i)
        return ret


class Test(unittest.TestCase):
    def setUp(self):
        self.arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]

    def tearDown(self):
        pass

    def test_checkZeroSum(self):
        exam = zeroSumSubArray(self.arr)
        self.assertTrue(exam.checkZeroSum())

    def test_zeroSumList(self):
        exam = zeroSumSubArray(self.arr)
        trueResult = [[3, 4, -7], [4, -7, 3], [-7, 3, 1, 3],
                      [3, 1, -4], [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]]
        self.assertTrue(sorted(exam.zeroSumList()) == sorted(trueResult))


if __name__ == "__main__":
    unittest.main()

import unittest
# Naive solution to find maximum product of two integers in a list


class solution:
    def findMaximumProductV1(self, arr):
        # O(n^2)
        maxProd = float('-inf')
        max_i, max_j = -1, -1

        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if maxProd < arr[i]*arr[j]:
                    maxProd = arr[i]*arr[j]
                    max_i, max_j = i, j
        return ((arr[max_i], arr[max_j]))

    def findMaximumProductV2(self, arr):
        # O(nlogn)
        arr = sorted(arr)
        if arr[0]*arr[1] < arr[-2]*arr[-1]:
            return (arr[-2], arr[-1])
        return (arr[0], arr[1])

    def findMaximumProductV3(self, arr):
        # O(n)
        # to store maximum and second maximum element in a list
        max1, max2 = arr[0], float('-inf')

        # to store minimum and second minimum element in a list
        min1, min2 = arr[0], float('inf')

        for val in arr[1:]:
            # if current element is more than the maximum element,
            # update maximum and second maximum element
            if val > max1:
                max2 = max1
                max1 = val
        # if current element is less than maximum but greater than
        # second maximum element, update second maximum element
            elif val > max2:
                max2 = val
        # if current element is more than the minimum element,
        # update minimum and second minimum element
            if val < min1:
                min2 = min1
                min1 = val
        # if current element is less than minimum but greater than
        # second minimum element, update second minimum element
            elif val < min2:
                min2 = val

        if max1*max2 > min1*min2:
            return (max1, max2)
        return (min1, min2)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This runs before all test
        print('SetUpClass')

    @classmethod
    def tearDownClass(cls):
        # This runs after all test is run
        print('tearDownClass')

    def setUp(self):
        # This run before each test
        self.arr = [-10, -3, 5, 6, -2]
        self.exam = solution()

    def tearDown(self):
        # This runs after each test
        pass

    def test_findMaximumProductV1(self):
        self.assertEqual(self.exam.findMaximumProductV1(self.arr), (-10, -3))

    def test_findMaximumProductV2(self):
        self.assertEqual(self.exam.findMaximumProductV2(self.arr), (-10, -3))

    def test_findMaximumProductV3(self):
        self.assertEqual(self.exam.findMaximumProductV3(self.arr), (-10, -3))


if __name__ == '__main__':
    unittest.main()

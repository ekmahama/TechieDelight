# Function to find maximum length sublist having equal number of 0's and 1's
# Function to find maximum length sublist having equal number of 0's and 1's
import unittest


def maxZeroOnesSubArr(arr):
    sum = 0
    dict = {}
    dict[sum] = -1
    length = 0
    end_index = -1
    # Set all 0 to -1 and find the max len subarray summing to 0
    # for i, val in enumerate(arr):
    #     if not val:
    #         arr[i]=-1

    for i, val in enumerate(arr):
        sum += -1 if not val else 1
        if sum not in dict:
            dict[sum] = i
        if sum in dict and length < i-dict[sum]:
            length = i-dict[sum]
            end_index = i

    if end_index != -1:
        return (end_index - length + 1, end_index)
    return []


class Test(unittest.TestCase):
    def setUp(self):
        self.arr = [0, 0, 0, 0, 0, 0, 0]
        self.arr1 = [1, 1, 1, 1, 1, 1, 1]
        self.arr2 = [0, 1, 0, 1, 0, 1, 0]
        self.arr3 = [0, 0, 0, 1, 1, 1, 0]

    def tearDown(self):
        pass

    def test_maxZeroOnesSubArr(self):
        self.assertEqual(maxZeroOnesSubArr(self.arr), [])
        self.assertEqual(maxZeroOnesSubArr(self.arr1), [])
        self.assertEqual(maxZeroOnesSubArr(self.arr2), (0, 5))
        self.assertEqual(maxZeroOnesSubArr(self.arr3), (0, 5))


if __name__ == '__main__':
    unittest.main()

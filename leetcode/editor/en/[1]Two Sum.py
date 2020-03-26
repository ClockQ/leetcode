# Given an array of integers, return indices of the two numbers such that they a
# dd up to a specific target. 
# 
#  You may assume that each input would have exactly one solution, and you may n
# ot use the same element twice. 
# 
#  Example: 
# 
#  
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#  
#  Related Topics Array Hash Table


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def brute_force(self, nums, target):
        """
        最基础的暴力破解

        TC = O(n^2)
        SC = O(1)
        """
        length = len(nums)
        for x in range(0, length):
            for y in range(x+1, length):
                if nums[x] + nums[y] == target:
                    return [x, y]
        return None

    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None

# leetcode submit region end(Prohibit modification and deletion)

# test case
import unittest

class TestCase(unittest.TestCase):
    def test_brute_force(self):
        tester = Solution()
        self.assertEqual(tester.brute_force([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(tester.brute_force([2, 2, 7, 11, 19, 9, 15], 9), [0, 2])

if __name__ == '__main__':
    unittest.main()

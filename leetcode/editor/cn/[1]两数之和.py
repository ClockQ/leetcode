# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
#  示例:
#
#  给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#
#  Related Topics 数组 哈希表


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

    def two_pass_hash_table(self, nums, target):
        """
        通过以空间换取速度的方式，我们可以将查找时间从 O(n) 降低到 O(1)。

        在第一次迭代中，我们将每个元素的值和它的索引添加到表中。
        然后，在第二次迭代中，我们将检查每个元素所对应的目标元素（target - nums[i]）是否存在于表中。
        注意，该目标元素不能是 nums[i] 本身！

        :raise 如果存在相同数字，返回的索引会优先使用大的

        TC = O(n)
        SC = O(n)
        """
        length = len(nums)
        hashmap = {}
        for x in range(0, length):
            hashmap[nums[x]] = x

        for x in range(0, length):
            res = target - nums[x]
            if res in hashmap and hashmap[res] != x:
                return [x, hashmap[res]]

        return None

    def one_pass_hash_table(self, nums, target):
        """
        对上面方法的一次改进，不需要先转换成 hash table。
        而是可以在转换的同时，直接检查之前的 hash 中是否存在可匹配的键。

        @notice 1. 注意 return 的先后顺序
        @notice 2. 当重复值存在时，不需要插入新的索引

        TC = O(n)
        SC = O(n)
        """
        hashmap = {}
        for x in range(0, len(nums)):
            res = target - nums[x]
            if res in hashmap:
                return [hashmap[res], x]
            elif nums[x] not in hashmap:
                hashmap[nums[x]] = x

    def one_pass_hash_table_by_enumerate(self, nums, target):
        """
        又是对上述方法的小改进，利用 enumerate 替换 for x in range(0, len(nums)) 即可。

        TC = O(n)
        SC = O(n)
        """
        hashmap = {}
        for x, num in enumerate(nums):
            res = target - num
            if res in hashmap:
                return [hashmap[res], x]
            elif num not in hashmap:
                hashmap[nums[x]] = x

    def twoSum(self, nums, target):
        return self.one_pass_hash_table_by_enumerate(nums, target)

# leetcode submit region end(Prohibit modification and deletion)

# test case
import unittest

class TestCase(unittest.TestCase):
    def test_brute_force(self):
        tester = Solution()
        self.assertEqual(tester.brute_force([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(tester.brute_force([2, 2, 7, 11, 19, 9, 15], 9), [0, 2])
        self.assertEqual(tester.brute_force([4, 2, 6, 11, 19, 9, 15], 8), [1, 2])

    def test_two_pass_hash_table(self):
        tester = Solution()
        self.assertEqual(tester.two_pass_hash_table([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(tester.two_pass_hash_table([2, 2, 7, 11, 19, 9, 15], 9), [0, 2])
        self.assertEqual(tester.two_pass_hash_table([4, 2, 6, 11, 19, 9, 15], 8), [1, 2])

    def test_one_pass_hash_table(self):
        tester = Solution()
        self.assertEqual(tester.one_pass_hash_table([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(tester.one_pass_hash_table([2, 2, 7, 11, 19, 9, 15], 9), [0, 2])
        self.assertEqual(tester.one_pass_hash_table([4, 2, 6, 11, 19, 9, 15], 8), [1, 2])

    def test_one_pass_hash_table_enumerate(self):
        tester = Solution()
        self.assertEqual(tester.one_pass_hash_table([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(tester.one_pass_hash_table([2, 2, 7, 11, 19, 9, 15], 9), [0, 2])
        self.assertEqual(tester.one_pass_hash_table([4, 2, 6, 11, 19, 9, 15], 8), [1, 2])

if __name__ == '__main__':
    unittest.main()

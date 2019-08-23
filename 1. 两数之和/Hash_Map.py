class Solution:
    """
    时间复杂度是 O(n)
    """
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return [0]
        hash_map = dict()
        for i, x in enumerate(nums):
            if target - x in hash_map:
                return [hash_map[target - x], i]
            hash_map[x] = i
        return [0]

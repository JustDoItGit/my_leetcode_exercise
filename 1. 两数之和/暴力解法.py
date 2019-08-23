class Solution:
    """
    复杂度 O(N2)
    """
    def twoSum(self, nums, target):
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if n + m == target and i < j:
                    return [i, j]
        return [0]

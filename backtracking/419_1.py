# 全排列 I
# 给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。
class Solution:
    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:

        def func(nums, n):
            if n == len(nums):
                self.result.append(nums[:])
            for i in range(n, len(nums)):
                nums[i], nums[n] = nums[n], nums[i]

                func(nums, n + 1)

                nums[i], nums[n] = nums[n], nums[i]

        func(nums, 0)
        return self.result
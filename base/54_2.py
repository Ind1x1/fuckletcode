# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        maxlen = 1
        ans = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # 跳过重复元素
            elif nums[i] == nums[i - 1] + 1:
                ans += 1
            else:
                maxlen = max(maxlen, ans)
                ans = 1  # 重置当前连续长度

        return max(maxlen, ans)

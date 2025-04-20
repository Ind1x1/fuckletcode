# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0  # 能跳到的最远距离
        for i in range(len(nums)):
            if i > farthest:
                return False  # 当前点无法到达
            farthest = max(farthest, i + nums[i])
        return True

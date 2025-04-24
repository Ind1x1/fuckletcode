# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的 子集（幂集）。
#
# 解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # 必须排序，才能识别重复元素

        def backtrack(start, path):
            res.append(path[:])  # 所有长度都可以添加，不需要 k 控制
            for i in range(start, len(nums)):
                # 跳过重复：当前值和上一个相同，且是在同一层递归中
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res
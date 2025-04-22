#给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

#解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path, k):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1, path, k)
                path.pop()

        res.append([])
        for i in range(1,len(nums)+1):
            backtrack(0,[],i)

        return res


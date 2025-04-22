#给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

#不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        dic = dict()
        while i<len(nums)-1:
            if nums[i] == nums[i+1] and not nums[i] in dic:
                dic[nums[i]] = True
                i += 1
            elif nums[i] == nums[i+1] and nums[i] in dic:
                nums.pop(i)
            else:
                i +=1
        return(len(nums))
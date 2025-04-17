# 最长不重复字符串
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# abcdebd
# abcde

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = dict()
        max_len = 0
        left = 0
        for id, char in enumerate(s):
            if char in temp and temp[char] >= left:
                left = temp[char] + 1
            temp[char] = id
            max_len = max(max_len, id - left + 1)
        return max_len


# abcbd

# abc

# cbd
# 字母异位词分组
# 你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d[''.join(sorted(s))].append(s)  # sorted(s) 相同的字符串分到同一组
        return list(d.values())

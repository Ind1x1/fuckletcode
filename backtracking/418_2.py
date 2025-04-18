# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # n 对括号意味着有 n 个 "（" 和 n个 “）”
        # 回溯法
        result = []

        def func(curr: str, left, right):
            if len(curr) == 2 * n:
                result.append(curr)

            if left < n:
                func(curr + "(", left + 1, right)

            if left > right:
                func(curr + ")", left, right + 1)

        func("", 0, 0)
        return result
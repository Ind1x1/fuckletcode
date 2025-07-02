# 请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
#
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

class Solution:
    def isValidSudoku(self, board):
        n = 9
        row = [set() for _ in range(n)]
        col = [set() for _ in range(n)]
        grid = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                num = board[r][c]
                idx = r // 3 * 3 + c // 3  # 3x3宫格索引计算
                if num in row[r] or num in col[c] or num in grid[idx]:
                    return False
                row[r].add(num)
                col[c].add(num)
                grid[idx].add(num)
        return True
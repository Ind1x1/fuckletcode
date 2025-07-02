# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])

        x = set()
        y = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 :
                    x.add(i)
                    y.add(j)

        for i in range(n):
            for j in range(m):
                if i in x or j in y : matrix[i][j] = 0
        return matrix

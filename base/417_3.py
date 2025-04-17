# Z 字形变换

# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        list = [ [] for i in range(numRows) ]
        _list = []
        i = 0
        flag = 1
        for id, char in enumerate(s):
            list[i].append(char)
            i += flag
            if i == numRows:
                flag = -1 * flag
        for i in range(numRows):
            _list = _list + list[i]
        return "".join(_list)

# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that the robot can take to
# reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# --------------- Runtime 34 ms, beats 60.66%. Memory 13.8MB, beats 65.16% ---------------


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n < 2:
            return n

        n = n - 1
        row = [1] * n
        for i in range(m - 1):
            next_row = [1] * n
            for j in range(n):
                next_row[j] = next_row[j - 1] + row[j]

            row = next_row
        return row[-1]

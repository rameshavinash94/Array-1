'''
Time Complexity : O(m*n) where m is the number of rows and n is the number of columns
Space Complexity : O(1) as we are not using any extra space
Did this code successfully run on Leetcode : Yes (#498)
Any problem you faced while coding this : No
'''
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat:
            return []
        rows, columns = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        direction = 1

        while len(result) < rows * columns:
            result.append(mat[r][c])
            if direction == 1:
                if c == columns - 1:
                    r += 1
                    direction = -1
                elif r == 0:
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == rows - 1:
                    c += 1
                    direction = 1
                elif c == 0:
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1

        return result
    
# Driver code
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.findDiagonalOrder(matrix)) # [1,2,4,7,5,3,6,8,9]
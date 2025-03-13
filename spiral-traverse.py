'''
Time Complexity : O(m*n) where m is the number of rows and n is the number of columns
Space Complexity : O(1) as we are not using any extra space
Did this code successfully run on Leetcode : Yes (#54)
Any problem you faced while coding this :  No
Approach:
# Traverse from left to right
# Traverse down
# Traverse from right to left
# Traverse up
# ensure that we are not traversing the same row or column again by checking if up != down and left != right
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse down
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            if up != down:
                # Traverse from right to left
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            if left != right:
                # Traverse up
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
    
# Driver code
sol = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix)) # [1,2,3,6,9,8,7,4,5]
        
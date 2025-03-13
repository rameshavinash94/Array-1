'''
Time Complexity : 0(n)
Space Complexity : 0(1) - no extra space used other than the output array
Did this code successfully run on Leetcode : Yes (# 238)
Any problem you faced while coding this : No
Approach:
- Initialize a product array with 1s of same length as input array
- Traverse the array from left to right and keep track of product of all elements to the left of current element
- Traverse the array from right to left and keep track of product of all elements to the right of current element
- Multiply the left product and right product to get the final product array
'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        product = [1] * l
        for i in range(1, l):
            product[i] = product[i-1] * nums[i-1]
        prev = 1
        for i in range(l-2,-1,-1):
            prev *= nums[i+1]
            product[i] = product[i] * prev

        return product
    
#Driver code
sol  = Solution()
print(sol.productExceptSelf([1,2,3,4])) # [24,12,8,6]
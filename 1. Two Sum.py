""" 1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up 
to target. You may assume that each input would have 
exactly one solution, and you may not use the same 
element twice. You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? """

from typing import List

class Solution:
    # Brute-force solution: Checks all possible pairs
    def twoSumSlow(self, nums: List[int], target: int) -> List[int]:
        # Iterate over all elements in nums
        for i in range(len(nums)):
            # For each element, iterate over all other elements
            for j in range(len(nums)):
                # Skip if it's the same element
                if i == j:
                    continue
                
                # Check if the sum of nums[i] and nums[j] equals the target
                if nums[i] + nums[j] == target:
                    # Return the indices if a match is found
                    return [i, j]
    
    # Improved solution: Avoids redundant comparisons
    def twoSumFast(self, nums: List[int], target: int) -> List[int]:
        # Iterate over all elements in nums
        for i in range(len(nums)):
            # Only check elements after the current index
            for j in range(i + 1, len(nums)):
                # Check if the sum of nums[i] and nums[j] equals the target
                if nums[i] + nums[j] == target:
                    # Return the indices if a match is found
                    return [i, j]

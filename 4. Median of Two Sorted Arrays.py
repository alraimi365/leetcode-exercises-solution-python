""" 4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays. The overall run time 
complexity should be O(log (m+n)). 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-10**6 <= nums1[i], nums2[i] <= 10**6 """

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Initialize variables to store the merged list and indices for each array
        merged_list = []  # Stores the merged result of nums1 and nums2
        nums1_ind = 0  # Pointer for nums1
        nums2_ind = 0  # Pointer for nums2
        
        # Merge the two arrays until all elements are processed
        while True:
            # Get the current element from nums1 and nums2 or assign a very large number
            # if the pointer exceeds the array length (acts as a boundary condition)
            num1 = nums1[nums1_ind] if nums1_ind < len(nums1) else (10**6) + 1
            num2 = nums2[nums2_ind] if nums2_ind < len(nums2) else (10**6) + 1

            # Compare the two numbers and append the smaller one to the merged list
            if num1 < num2:
                merged_list.append(num1)
                nums1_ind += 1  # Increment nums1 pointer
            else:
                merged_list.append(num2)
                nums2_ind += 1  # Increment nums2 pointer

            # Exit the loop when both arrays are fully processed
            if nums1_ind >= len(nums1) and nums2_ind >= len(nums2):
                break
        
        # Find the median of the merged array
        # Calculate the middle index (supports float for even-length arrays)
        med = float(len(merged_list) / 2)
        
        # Check if the length of the merged list is even
        if med % 1 == 0:  # Even-length array
            n1 = merged_list[int(med)]  # Right middle element
            n2 = merged_list[int(med) - 1]  # Left middle element
            return (n1 + n2) / 2.0  # Median is the average of the two middle elements
        else:  # Odd-length array
            return merged_list[int(med)]  # Median is the middle element

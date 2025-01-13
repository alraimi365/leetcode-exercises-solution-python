""" 2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single 
digit. Add the two numbers and return the sum as a linked list. You may assume 
the two numbers do not contain any leading zero, except the number 0 itself. 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros. """

from typing import List, Optional

# Definition for a singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Original solution with a less efficient approach
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0  # Carry-over for digit sums greater than 9
        rem_linked_list = None  # Stores the remaining list when one ends
        tail = None  # Tail of the result list (constructed in reverse)

        while True:
            # Add the digits of the current nodes and the carry
            temp_sum = list(str(l1.val + l2.val + carry))
            
            # Extract carry and current digit from the sum
            if len(temp_sum) == 2:  # Sum is two digits
                carry = int(temp_sum[0])  # Carry is the tens place
                val = int(temp_sum[1])  # Digit is the ones place
            else:
                carry = 0  # No carry
                val = int(temp_sum[0])  # Single-digit sum
            
            # Prepend the current digit to the result list
            tail = ListNode(val, tail)
            
            # Move to the next nodes in the lists
            l1 = l1.next
            l2 = l2.next

            # Check if both lists are exhausted
            if l1 is None and l2 is None:
                if carry > 0:  # Add the final carry if it exists
                    tail = ListNode(carry, tail)
                break
            elif l1 is None:  # If l1 is exhausted, process the remaining l2
                rem_linked_list = l2
                break
            elif l2 is None:  # If l2 is exhausted, process the remaining l1
                rem_linked_list = l1
                break

        # Process the remaining list if one list was longer
        while rem_linked_list is not None:
            temp_sum = list(str(carry + rem_linked_list.val))
            if len(temp_sum) == 2:  # Handle carry-over
                carry = int(temp_sum[0])
                val = int(temp_sum[1])
            else:
                carry = 0
                val = int(temp_sum[0])

            tail = ListNode(val, tail)
            rem_linked_list = rem_linked_list.next

            # Add the final carry if needed
            if rem_linked_list is None and carry > 0:
                tail = ListNode(carry, tail)
                break

        # Reverse the result list to get the correct order
        head = ListNode(tail.val, None)
        tail = tail.next
        while tail is not None:
            head = ListNode(tail.val, head)
            tail = tail.next

        return head

    # Optimized solution using a dummy head for simpler list construction
    def addTwoNumbersEfficient(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0  # Carry-over for digit sums greater than 9
        dummy_head = ListNode(0)  # Dummy node to simplify list construction
        curr = dummy_head  # Pointer to the current node in the result list

        # Process both lists and any remaining carry
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if the list is exhausted
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Compute the digit and the carry using divmod
            carry, val = divmod(val1 + val2 + carry, 10)
            
            # Add the new digit as a node in the result list
            curr.next = ListNode(val)
            curr = curr.next
            
            # Move to the next nodes in the lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Return the result list, starting after the dummy head
        return dummy_head.next

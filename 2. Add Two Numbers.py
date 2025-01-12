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

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        rem_linked_list = None
        tail = None

        while(1):
            temp_sum = list(str(l1.val + l2.val + carry))
            
            if len(temp_sum) == 2:
                carry = int(temp_sum[0])
                val = int(temp_sum[1]) 
            else:
                carry = 0
                val = int(temp_sum[0])
            
            tail = ListNode(val, tail)
            l1 = l1.next
            l2 = l2.next

            if l1 == None and l2 == None:
                if carry > 0 :
                    tail = ListNode(carry, tail)
                break
            elif  l1 == None:
                rem_linked_list = l2
                break 
            elif l2 == None:
                rem_linked_list = l1
                break 

        while(rem_linked_list is not None):

            temp_sum = list(str(carry + rem_linked_list.val))
            if len(temp_sum) == 2:
                carry = int(temp_sum[0])
                val = int(temp_sum[1]) 
            else:
                carry = 0
                val = int(temp_sum[0])

            tail = ListNode(val, tail)
            rem_linked_list = rem_linked_list.next

            if rem_linked_list == None:
                if carry > 0 :
                    tail = ListNode(carry, tail)
                break
        
        head = ListNode(tail.val, None)
        tail = tail.next
        while (tail is not None):
            head = ListNode(tail.val, head)
            tail = tail.next
        
        return head
    
    def addTwoNumbersEfficient(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode(0)
        curr = dummy_head

        while(l1 or l2 or carry):

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            carry, val = divmod(val1 + val2 + carry, 10)
            
            curr.next = ListNode(val)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy_head.next
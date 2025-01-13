""" 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces """

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        s_ind = 0
        word = []
        optim_len = 0

        if len(s) == 0:
            return 0
        
        while(1):
            rep_flag = False
            letter = s[s_ind]

            for l2 in range(len(word)):
                if letter == word[l2]:
                    rep_flag = True
                    break
            
            if rep_flag:

                if len(word) > optim_len:
                    optim_len = len(word)
    
                s_ind = s_ind - (len(word)-l2)
                word = []
            else:
                word.append(letter)

            s_ind += 1

            if s_ind >= len(s):
                break
        
        if len(word) > optim_len:
            optim_len = len(word)
        
        return optim_len
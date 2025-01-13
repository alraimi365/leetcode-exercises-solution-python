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
        # Initialize the starting index of the current substring
        s_ind = 0
        # List to store the characters of the current substring
        word = []
        # Variable to store the length of the longest substring found
        optim_len = 0

        # Edge case: If the string is empty, the result is 0
        if len(s) == 0:
            return 0
        
        # Loop to process the entire string
        while True:
            rep_flag = False  # Flag to check for repeated characters
            letter = s[s_ind]  # Current character being processed

            # Check if the current character is already in the substring
            for l2 in range(len(word)):
                if letter == word[l2]:
                    # Mark that a repeated character is found
                    rep_flag = True
                    break
            
            if rep_flag:
                # Update the longest substring length if the current substring is longer
                if len(word) > optim_len:
                    optim_len = len(word)
    
                # Move the starting index to the right of the repeated character
                s_ind = s_ind - (len(word) - l2)
                # Reset the current substring
                word = []
            else:
                # Add the current character to the substring
                word.append(letter)

            # Move to the next character in the string
            s_ind += 1

            # Break the loop when the end of the string is reached
            if s_ind >= len(s):
                break
        
        # Final check: Update the longest substring length if the last substring is the longest
        if len(word) > optim_len:
            optim_len = len(word)
        
        # Return the length of the longest substring without repeating characters
        return optim_len

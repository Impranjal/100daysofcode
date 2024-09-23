#User function Template for python3

"""Program to find string is palindrome or not"""
class Solution:
    def isPalindrome(self, S):
        left = 0
    
        right = len(S)-1
        while left <= right:
            if S[left] != S[right]:
                return 0
            else:
                left,right= left+1,right-1
        
        return 1
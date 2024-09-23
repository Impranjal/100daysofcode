#User function Template for python3
"""The problem is abouth reversing the string"""
class Solution:
     def reverseWord(self, str: str) -> str:
        #your code here
        new_str =''.join(str[::-1])
        return new_str
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while(t>0):
        s = input()
        ob = Solution()
        print(ob.reverseWord(s))
        t = t-1

# } Driver Code Ends
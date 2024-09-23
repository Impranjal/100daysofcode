#User function Template for python3
"""The problem is given two array find the union of the array"""
class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,arr1,arr2):
        set1 = set()
        set1.update(arr1)
        set1.update(arr2)
        n = len(set1)
        return n
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.doUnion(a, b))

# } Driver Code Ends
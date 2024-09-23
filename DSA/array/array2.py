"""Program to get second largest no in array"""

class Solution:
    def getSecondLargest(self, arr):
        large = 0
        sec_large =-1
        for i in arr:
            if i > large:
                large = i
        for i in range(len(arr)):
            if arr[i] >sec_large and arr[i] <large:
                sec_large = arr[i]
        return sec_large
        # Code Here
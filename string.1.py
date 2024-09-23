def getConcatenation(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = list(range(2*n))
        print(arr)
        for i in range(2*n):
            if i < n:
                arr[i] = nums[i]
            elif i >=n:
                print(i)
                arr[i] = arr[i-n]
        return arr

nums = [1,2,1]
print(getConcatenation(nums))
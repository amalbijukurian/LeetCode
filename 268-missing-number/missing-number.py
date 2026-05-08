class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        for i in range(n+1):
            if i not in nums:
                mis=i
        return mis
        
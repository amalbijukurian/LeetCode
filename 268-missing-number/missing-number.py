class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expec=n*(n+1)//2
        act=sum(nums)
        return expec-act
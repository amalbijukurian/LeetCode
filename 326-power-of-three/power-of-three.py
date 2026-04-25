class Solution(object):
    def isPowerOfThree(self, n):
        if n<=0:
            return False
        else:
            pow=1
            while pow<n:
                pow*=3
            if pow==n:
                return True
            else:
                return False
        
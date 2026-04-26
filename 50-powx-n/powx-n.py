class Solution(object):
    def myPow(self, x, n):
        res = 1
        
        if n < 0:
            x = 1 / x
            n = -n
        
        while n:
            if n % 2:
                res *= x
            x *= x
            n //= 2
        
        return res
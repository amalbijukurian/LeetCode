class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            rev=0
            st=x
            while x>0:
                temp=x%10
                rev=rev*10+temp
                x=x/10
            if st==rev:
                return True
            else:
                return False

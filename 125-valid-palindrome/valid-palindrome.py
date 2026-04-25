class Solution(object):
    def isPalindrome(self, s):
        if s=="":
            return True
        else:

            strs="".join(char for char in s if char.isalnum())
            st=strs.lower()
            if st==st[::-1]:
                return True
            else:
                return False

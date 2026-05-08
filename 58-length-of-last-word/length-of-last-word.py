class Solution(object):
    def lengthOfLastWord(self, s):
        sp=s.split()
        return len(sp[-1])


    
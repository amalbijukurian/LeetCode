class Solution(object):
    def isAnagram(self, s, t):
        alpha=[0]*26
        for ch in s:
            alpha[ord(ch) - ord('a')] +=1
        for ch in t:
            alpha[ord(ch)-ord('a')] -=1
        for i in alpha:
            if i!=0:
                return False
        return True
        
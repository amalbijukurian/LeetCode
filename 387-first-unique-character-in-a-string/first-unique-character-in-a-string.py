class Solution(object):
    def firstUniqChar(self, s): 
        freq = {}
        
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        
        return -1
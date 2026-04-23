class Solution(object):
    def findWordsContaining(self, words, x):
        ls=[]
        for i in range(len(words)):
            if x in words[i]:
                ls.append(i)
        return ls


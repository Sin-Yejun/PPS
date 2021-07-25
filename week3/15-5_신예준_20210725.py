class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)>len(t):
            return False
        if len(s) == 0:
            return True
        index = 0
        
        for i in t:
            if index < len(s) and s[index] == i:
                index +=1
        if index == len(s):
            return True

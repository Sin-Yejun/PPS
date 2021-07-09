class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        output = 0
        g.sort()
        s.sort()
        for i in range(len(s)):
            for j in range(len(g)):
                if s[i] >= g[j]:
                    del g[j]
                    output +=1
                    break
            if(output ==  len(s)):
                return output
        return output

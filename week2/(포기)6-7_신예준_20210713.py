class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(map(str,s))
        result =''
        flag = False
        ct = 0
        while flag != True:
            flag = True
            result = ''
            ct = 0
            while True:
                if(len(s)==0):
                    break
                if ct != len(s)-1 and s[ct] == s[ct+1]:
                    ct+=2
                    flag = False
                    if ct >= len(s):
                        break
                result += s[ct]
                ct +=1
                if ct >= len(s):
                    break
            s = result
        return result

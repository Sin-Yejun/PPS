class Solution:
    def addDigits(self, num: int) -> int:
        s= 0
        while True:
            while num!=0:
                a = num % 10
                s += a
                num = num//10
            num = s
            if s//10 == 0:
                break
            s = 0
        return s

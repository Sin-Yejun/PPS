def is_digit(str):
    try:
        tmp = float(str)
        return True
    except ValueError:
        return False
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        li = []
        x = 0
        for i in ops:
            if is_digit(i):
                li.append(int(i))
            elif i == 'C':
                del li[-1]
            elif i == 'D':
                x = li[-1] * 2
                li.append(x)
            elif i == '+':
                x = li[-1] + li[-2]
                li.append(x)
        return sum(li)

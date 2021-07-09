import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<1:
            return False
        a = "{:g}".format(math.log(n,4))
        if a.isnumeric():
            return True
        else:
            return False

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        size = len(digits)-1
        for i in range(len(digits)):
            number += digits[i]*(10**size)
            size -= 1
        number += 1
        output = []
        output = list(map(int,str(number)))
        return output

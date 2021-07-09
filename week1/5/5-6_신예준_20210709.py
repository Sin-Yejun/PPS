class Solution:
    def isPalindrome(self, s: str) -> bool:
        p = ''
        for i in s:
            if i.isalpha():
                p += i.lower()
            elif i.isdigit():
                p += str(i)
        if p[::-1] == p:
            return True
        else:
            return False

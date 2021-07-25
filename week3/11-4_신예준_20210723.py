class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        length = nums
        length.sort()
        n = len(length)
        for i in range(n-1, 1, -1):
            if length[i-2] + length[i-1] > length[i]:
                return length[i-2] + length[i-1] + length[i]
        return 0

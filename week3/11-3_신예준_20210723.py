class NumArray:

    def __init__(self, nums: List[int]):
        self.li = nums
        self.sum = 0
    def sumRange(self, left: int, right: int) -> int:
        self.sum=0
        for i in range(left,right+1):
            self.sum += self.li[i]
        return self.sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

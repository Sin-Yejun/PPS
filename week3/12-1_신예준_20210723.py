class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        d = [-1 for i in range(len(nums))]
        even = 0
        odd = 1
        for i in range(len(nums)):
            if nums[i] %2 ==0:
                d[even] = nums[i]
                even +=2
            if nums[i] %2==1:
                d[odd] = nums[i]
                odd +=2
        return d

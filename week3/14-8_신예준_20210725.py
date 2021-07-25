class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        d = []
        for i in range(len(nums)):
            r = False
            
            for j in range(1, len(nums)):
                if nums[(i+j) % len(nums)] > nums[i]:
                    d.append(nums[(i+j) % len(nums)])
                    r = True
                    break
            if r == False:
                d.append(-1)
        return d

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    x = nums2[j]
                    r = -1
                    for k in range(j,len(nums2)):
                        if nums2[k] > x:
                            r = nums2[k]
                            li.append(r)
                            break
                    if r == -1:
                        li.append(r)
        return li

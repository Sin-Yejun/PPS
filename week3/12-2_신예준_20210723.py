class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        else:
            for i in range(n):
                nums1[m] = nums2[i]
                m+=1
            nums1.sort()

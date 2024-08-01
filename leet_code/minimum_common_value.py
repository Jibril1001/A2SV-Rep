class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i,j=0,0
        while len(nums1)>i and len(nums2)>j:
            if nums1[i]==nums2[j]:
                return nums1[i]
            if nums1[i]<nums2[j]:
                i=1+i
            else:
                j=j+1
        
        return -1
        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nm1=copy.deepcopy(nums1)
        i,n2index,n1index=0,0,0
        while i<(m+n):
            if  n1index<m and (n2index>=n or  nm1[n1index]<nums2[n2index]):
                nums1[i]=nm1[n1index]
                n1index=n1index+1
            else:
                nums1[i]=nums2[n2index]
                n2index=n2index+1
            i=i+1

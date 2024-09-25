class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0]>=k:return 0
        sum,i,j=0,0,len(nums)-1
        while i<j:
            if nums[j]>=k or nums[j]+nums[i]>k:
                j=j-1
            elif nums[j]+nums[i]<k:
                i=i+1
            elif nums[j]+nums[i]==k:
                sum=sum+1
                i=i+1
                j=j-1
        return sum
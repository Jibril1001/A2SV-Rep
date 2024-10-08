class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,zeros,total=0,0,0
        for j in range(len(nums)):
            if nums[j]==0:
                zeros+=1
            if zeros>k:
                if nums[i]==0:
                    zeros-=1
                    i+=1
                else:
                    while i<j and nums[i]==1:
                        i+=1
                    i+=1
                    zeros-=1
            total=max(total,j-i+1)
        return total
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k-1
        total=0
        s=0
        while j<len(nums):
            if i==0:
                total=sum(nums[i:j+1])
                s=total
                i+=1
                j+=1
            else:
                s=s-nums[i-1]+nums[j]
                total=max( s,total )
                i+=1
                j+=1
        return total/k
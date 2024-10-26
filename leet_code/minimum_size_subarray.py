class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        su,si=0,0
        cl=True
        while j<len(nums):
            if nums[j]==target: return 1
            if cl: su+=nums[j]
            if su>target:
                if si!=0:si=min(j-i+1,si)
                else: si=j-i+1
                su-=nums[i]
                i+=1
                cl=False
            elif su==target:
                if si!=0:si=min(j-i+1,si)
                else: si=j-i+1
                su-=nums[i]
                i+=1
                j+=1
                cl=True
            else:
                j+=1
                cl=True
        return si
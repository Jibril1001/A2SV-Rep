class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        zer=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=2*nums[i]
                nums[i+1]=0
                zer=zer+1
            if nums[i]==0:
                zer=zer+1
        while zer>0:
            nums.remove(0)
            nums.append(0)
            zer=zer-1
        return nums
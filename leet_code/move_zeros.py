class Solution(object):
    def moveZeroes(self, nums):
        s=0
        for i in range(len(nums)):
            if nums[i]==0:
                s+=1
        
        for i in range(s):
            nums.remove(0)
            nums.append(0)

           
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
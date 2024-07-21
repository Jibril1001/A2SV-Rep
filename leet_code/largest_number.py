class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums)
        print(nums)
        result = []
        n = 1
        j = 0
        for i in range(len(nums)):
            if nums[i] >= 10 ** n:
                print("done")
                print(nums[i - 1::-1])
                result.extend(nums[i - 1:j:-1])
                print(result)
                j = i - 1
                n+=1
        result.append(nums[-1])
        print(result)
        return ''.join(list(map(str, result)))

        

        
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num=[str(x) for x in nums]
        num.sort(key=cmp_to_key(lambda a,b: (b+a) > (a+b) or -1) )
        if num[0]=='0':
            return '0'
        return "".join(num)     
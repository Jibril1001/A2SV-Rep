class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if floor(sqrt(c))==sqrt(c):
            return True
        i=0
        j=floor(sqrt(c))
        while i<=j:
            if i**2 + j**2 > c:
                j=j-1
            elif i**2 + j**2 < c:
                i=i+1
            elif i**2 + j**2 == c:
                return True
        return False
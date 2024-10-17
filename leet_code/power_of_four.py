class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:return False
        if (n==1 or n==4) or self.isPowerOfFour(n/4):
            return True
        else:
            return False
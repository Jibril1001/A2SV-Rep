class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n==3 or n==1:
            return True
        if n<=0 or n%3!=0:
            return False
        else:
            return self.isPowerOfThree(n/3)       
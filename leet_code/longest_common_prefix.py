class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=min(strs,key=len)
        c=""
        for i in range(len(a)):
            for j in range(len(strs)):
                if a[i]!=strs[j][i]:
                    return c
            c=c + a[i]
        return c
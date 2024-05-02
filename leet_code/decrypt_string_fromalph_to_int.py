class Solution:
    def freqAlphabets(self, s: str) -> str:
        x= " abcdefghijklmnopqrstuvwxyz"
        p=""
        ans=""
        k=0
        for i in range(len(s)):
            if s[i]!='#' and k!=3:
                p=p+s[i]
                k=k+1
            elif s[i]=='#':
                if k==3:
                    ans = ans + x[int(p[0])]
                    p=p[1:]
                ans = ans + x[int(p)]
                p=""
                k=0
            if k==3 and s[i]!='#':
                ans= ans + x[int(p[0])]
                k=2
                p=p[1:]
        r=0
        while r<k:
            ans=ans+ x[int(p[r])]
            r=r+1
        return ans
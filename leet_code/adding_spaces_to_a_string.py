class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=[]
        spindex=0
        stindex=0
        num=0
        for i in range(len(s)+len(spaces)):
            if spindex!=len(spaces) and i==spaces[spindex]+num:
                ans.append(" ")
                spindex=spindex+1
                num=num+1
            else:
                ans.append(s[stindex])
                stindex=stindex+1
        return "".join(ans)
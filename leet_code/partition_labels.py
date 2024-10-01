class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        num={}
        dic={}
        ans=[]
        size=0
        partition=False
        for i in range(len(s)):
            if s[i] not in num.keys():
                num[s[i]]=1
            else:num[s[i]]=num[s[i]]+1
        for i in range(len(s)):
            size=size+1
            num[s[i]]=num[s[i]]-1
            if s[i] not in dic.keys():
                dic[s[i]]=0 
            if num[s[i]]==0:
                partition=True
                for key in dic:
                    if num[key]!=0:
                        partition=False
                        break
            if partition:
                dic={}
                ans.append(size)
                size=0
                partition=False
        return ans
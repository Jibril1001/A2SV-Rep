class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        i,j=0,0
        total=0
        while j<len(s):
            if s[j] in dic.keys() and dic[s[j]]>=i:
                total=max(total,j-dic[s[j]])
                i=dic[s[j]]+1
            else:total=max(total,j-i+1)
            dic[s[j]]=j
            j+=1
        return total

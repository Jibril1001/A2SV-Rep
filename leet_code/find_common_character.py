class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words[0])):
            a=True
            for j in range(1,len(words)):
                if words[0][i] not in words[j]:
                    a=False
                    break
            if a==True:
                for j in range(1,len(words)):
                    words[j].replace(words[0][i],'',1)
                print(words)
                ans.append(words[0][i])
        return ans
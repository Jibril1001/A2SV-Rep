class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        ans =[]
        index1=0
        index2=0
        for i in range(len(word1)+len(word2)):
            if word1[index1:]>word2[index2:]:
                ans.append(word1[index1])
                index1=index1+1
            else:
                ans.append(word2[index2])
                index2=index2+1
        return "".join(ans)
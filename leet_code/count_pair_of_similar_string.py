class Solution:
    def similarPairs(self, words: List[str]) -> int:
        word=["".join(sorted(set(words[i]))) for i in range(len(words))]
        word=sorted(word)
        t=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if word[i]==word[j]: t=t+1
                else: break
        return t
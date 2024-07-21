class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        sl=list(s)
        i=0
        j=len(sl)-1
        while i < j:
            if (sl[i] in vowels) and (sl[j] in vowels):
                sl[i],sl[j]=sl[j],sl[i]
                i=i+1
                j=j-1
            elif (sl[i] in vowels) and (sl[j] not in vowels):
                j=j-1
            elif (sl[i] not in vowels) and (sl[j] in vowels):
                i=i+1
            else :
                i=i+1
                j=j-1
        return ''.join(sl)

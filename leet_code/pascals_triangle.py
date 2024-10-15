class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls=[[1],[1,1]]
        if len(ls)>=numRows:
            return ls[:numRows]
        for i in range(2,numRows):
            sl=[1]*(i+1)
            for j in range(1,len(sl)-1):
                sl[j]=ls[i-1][j-1]+ls[i-1][j]
            ls.append(sl)
        return ls
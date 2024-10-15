class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ls=[[1],[1,1]]
        if len(ls)>=numRows:
            return ls[:numRows]
        last_list=self.generate(numRows-1)
        last_row=last_list[len(last_list)-1]
        cur=[[1]]
        for i in range(numRows-2):
          cur[0].append(last_row[i]+last_row[i+1])
        cur[0].append(1) 
        return last_list + cur
'''
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
    '''
 
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        ans=[ [0]*(len(grid)-2) for _ in range(len(grid[0])-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                sum=0
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if grid[k][l]>sum:
                            sum=grid[k][l]
                ans[i][j]=sum
        return ans
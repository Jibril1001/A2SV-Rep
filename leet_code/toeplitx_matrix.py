class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i!=0 and j!=0:
                    if i==j and matrix[i-1][j-1]!=matrix[i][j]:
                        return False
                    elif matrix[i-1][j-1]!=matrix[i][j]:
                        return False 

        return True
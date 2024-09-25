class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total=(sum(skill))/(len(skill)/2)
        ret,i,j=0,0,len(skill)-1
        while i<j:
            if skill[i]+skill[j]!=total:
                return -1
            ret=ret+(skill[i]*skill[j])
            i=i+1
            j=j-1
        return ret
        
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans=[[],[]]
        win={}
        for i in range(len(matches)):
            if matches[i][0] not in win.keys():
                win[matches[i][0]] = [0,0]
            if matches[i][1] not in win.keys():
                win[matches[i][1]] = [0,0]
            win[matches[i][0]] = [ win[ matches[i][0] ][0] + 1 , win[ matches[i][0] ][1] ]
            win[matches[i][1]] = [ win[ matches[i][1] ][0] , win[ matches[i][1] ][1] + 1 ]
        for i in win:
            if win[i][1]==0:
                ans[0].append(i)
            if win[i][1]==1:
                ans[1].append(i)
        ans[0].sort()
        ans[1].sort()
        return ans
        
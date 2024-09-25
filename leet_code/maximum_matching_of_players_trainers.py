class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        trainers.sort()
        players.sort()
        sum,i,j=0,0,0
        while j<len(trainers) and i<len(players):
            if players[i]>trainers[j]:j=j+1
            else:
                sum=sum+1
                i=i+1
                j=j+1
        return sum
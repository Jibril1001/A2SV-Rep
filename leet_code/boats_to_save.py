class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j=0,len(people)-1
        sum=0
        while i<j:
            if people[i]+people[j]>limit:
                j=j-1
                sum=sum+1
            elif people[i]+people[j]==limit:
                i=i+1
                j=j-1
                sum=sum+1
            elif people[i]+people[j]<limit:
                i=i+1
                j=j-1
                sum=sum+1
            if i==j:
                sum=sum+1
                break
        return sum
        """If there was no limit to the number of people that can get o the boat it would have been
class Solution:
     def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i,j=0,len(people)-1
        sum=0
        case=0
        while i<j:
            if people[i]+people[j]>limit:
                j=j-1
                sum=sum+1
            elif people[i]+people[j]==limit:
                i=i+1
                j=j-1
                sum=sum+1
                case=0 
            elif people[i]+people[j]<limit:
                case=people[i]+people[j]
                while case<limit and i<j:
                    i=i+1
                    case=people[i]+case
                j=j-1
                sum=sum+1
            if i==j:
                sum=sum+1
                break
        return sum

        """

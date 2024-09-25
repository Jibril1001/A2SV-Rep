class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums)
        print(nums)
        result = []
        n = 1
        j = 0
        for i in range(len(nums)):
            if nums[i] >= 10 ** n:
                print("done")
                print(nums[i - 1::-1])
                result.extend(nums[i - 1:j:-1])
                print(result)
                j = i - 1
                n+=1
        result.append(nums[-1])
        print(result)
        return ''.join(list(map(str, result)))

'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        numst=[str(num) for num in nums]
        numst.sort(key=lambda x:x[:1],reverse=True)
        print(numst)
        r=1
        size=1
        cont=False
        for i in range(len(numst)):
            if i!=0 and numst[i][0]==numst[i-1][0]:
                r=1+r
                size=max(len( numst[i-1][0]),len( numst[i][0]))
                cont=True
            elif cont==True:
                cont=False
                k,l,s=r.deepcopy(),i.deepcopy(),size.deepcopy()
                sortk(numst,k,l,s)
                r=1
        return numst

    def sortk( nums: List[String],r,i,size):
        for i in range(size):
            midlist=nums[]
            numst.sort(key=lambda x:x[:1],reverse=True)
   
   
   class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num=[str(x) for x in nums]
        num.sort(reverse=True)
        rep=1
        for i in range(len(num)):
            if i!=0 and num[i][0]==num[i-1][0]:
                rep=rep+1
            elif i!=0 and r>1:
                sortk(num,i,r)
                r=1
        return nums=[int(x) for x in num]
    def sortk(nums: List[String],i,r):
        nums[i-r+1,i+1].sort(key= lambda x:x[1])

class Solution:
    def sortk(num: List[String],i,rep):
        if i+1==len(num):
            if num[i-rep]==0: return
            for j in range(rep):
                print(num[i-j])
                if num[i-j]>=num[i-j-1][:-1]:
                    num[i-j-1],num[i-j]=num[i-j],num[i-j-1]
        else:
            for j in range(rep-1):
                if num[i-j-1]>=num[i-j-2][:-1]:
                    num[i-j-2],num[i-j-1]=num[i-j-1],num[i-j-2]

    def largestNumber(self, nums: List[int]) -> str:
        num=[str(x) for x in nums]
        num.sort(reverse=True)
        rep=1
        for i in range(len(num)):
            if i!=0 and num[i][0]==num[i-1][0] and i+1!=len(num):
                print("r")
                rep=rep+1
            elif (rep>1 and num[i][0]!=num[i-1][0] and len(num[i-1])==1) or ( i+1==len(num) and rep>1 and len(num[i])==1) :
                print("in")
                sortk(num,i,rep)
                rep=1
            else:
                rep=1
        return ''.join(num)

            #note you need to check  the second character(of first element) is smaller than the first characterof second element of len 1 (case 2 : 34,3 vs 32,3)        
'''

        
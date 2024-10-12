class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic={}
        total=0
        for i in range(len(s)):
            if s[i] not in dic.keys():dic[s[i]]=[i]
            else: dic[s[i]].append(i)

        for key in dic:
            total=max(total,1)
            f,num=0,dic[key][0] 
            size=1
            j=1
            while j<len(dic[key]):
                print("-------------------"+str(s))
                print(j)
                print(dic[key])
                print("Num: "+ str(num))
                print("F: "+str(f))
                print( "when diff and f<k: "+str(num+1!=dic[key][j] and f<k))
                print("when diff and f==k: "+str(num+1!=dic[key][j] and f==k))
                print(dic[key][j])
                print("total:"+str(total))
                if num+1!=dic[key][j] and f<k:
                    f+=1
                    num+=1
                    size+=1
                    total=max(total,size)
                elif num+1!=dic[key][j] and f==k:
                    #total=max(total,size+1)
                    f=0
                    j+=1
                    if j<len(dic[key]): num=dic[key][j]
                    size=1
                else:
                    j+=1
                    size+=1
                    num+=1
                    total=max(total,size)
                if f<k and j==len(dic[key]) and dic[key][j-1]!=len(s)-1:
                    print("in")
                    total=max(total,size+(k-f))
                print("Size: "+str(size))
                print("Total: "+str(total))
                print("-------------------")
        return total
#I tried iterating through the map but it was too difficult I hope I will return and finish this with time complexity of O(3n)
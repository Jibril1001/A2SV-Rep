def insertionSort1(n, arr):
    t=arr[len(arr)-1]
    for i in range(len(arr)-1,-1,-1):
        if i!=0 and arr[i-1]>=t:
            arr[i]=arr[i-1]
            print(*arr,sep=" ")
        elif i!=0 and t>arr[i-1]:
            arr[i]=t
            print(*arr,sep=" ")
            break
        elif i==0:
            arr[i]=t
            print(*arr,sep=" ")
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

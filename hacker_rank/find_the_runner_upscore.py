if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(key=None,reverse=True)
    for i in range(len(arr)):
        if arr[i]<arr[0]:
            print(arr[i])
            exit()
    print(arr[0])
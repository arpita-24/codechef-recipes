t = int(input())

for i in range(t):
    N,K = map(int,input().split(" "))
    lst = list(map(int,input().split(" ")))
    res = ""
    for i in range(N):
        if lst[i]<=K:
            K -= lst[i]
            res += "1"
        else:
            res += "0"
    print(res)

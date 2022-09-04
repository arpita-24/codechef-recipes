# cook your dish here
T = int(input())
for i in range(T):
    N = int(input())
    infect = list(map(int,input().split(" ")))
    mn = 999
    mx = -999
    yes = 1
    for i in range(1,N):
        diff = infect[i]-infect[i-1]
        # print(f"{infect[i]}-{infect[i-1]}={diff}")
        if diff<=2:
            yes += 1
            # print(yes)
        elif diff>2:
            if yes>mx:
                mx = yes
            
            if yes<mn:
                mn = yes
            yes = 1
            
    if yes>mx:
        mx = yes
    
    if yes<mn:
        mn = yes
        
    if yes==N:
        print(yes,yes)
    else:
        print(mn,mx)
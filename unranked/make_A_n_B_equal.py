T = int(input())
for i in range(T):
    A, B = map(int,input().split())
    
    if A == B:
        print("YES")
    else:
        if A<B:
            i = A
            mx = B
        else:
            i = B
            mx = A
            
        while i<mx:
            
            i = i * 2
        
        if i == mx:
            print("YES")
        else:
            print("NO")

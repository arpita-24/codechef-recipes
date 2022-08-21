t = int(input())
for i in range(t):
    n = int(input())
    dollsLeft = {}
    for j in range(n):
        typ = int(input())
        if typ in dollsLeft:
            dollsLeft[typ] += 1
        else:
            dollsLeft[typ] = 1
            
        
    for k,v in dollsLeft.items():
        if v%2 != 0:
            print(k)
            break

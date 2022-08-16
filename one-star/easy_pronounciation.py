consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    cnt = 0
    for j in range(n):
        if s[j] in consonants:
            cnt += 1
        else:
            cnt = 0
            
        if cnt >= 4:
            print("NO")
            break
    else:
        print("YES")

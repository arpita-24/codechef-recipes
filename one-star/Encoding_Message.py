# cook your dish here
t = int(input())

alpha = {'a':'z', 'b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}

for i in range(t):
    N = int(input())
    S = input()
    D = 25
    if N%2 == 0:
        res = [0]*N
    else:
        res = [0]*(N-1)
    for i in range(1,N,2):
        res[i] = S[i-1]
        res[i-1]= S[i]
    if N%2 != 0:
        res.append(S[-1])
   
    for i in range(len(res)):
        res[i] = alpha[res[i]]
        
    print("".join(res))
        
        
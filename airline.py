t= int(input())

while(t):
    a,b,c,d,e = map(int,(input()).split())
    if(a+b<=d and c<=e):
        print("YES")
    elif(c+b<=d and a<=e):
        print("YES")  
    elif(a+c<=d and b<=e):
        print("YES")
    else:
        print("NO")
    t=t-1
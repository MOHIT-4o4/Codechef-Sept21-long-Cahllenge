t =int(input())
while(t):
    n = int(input())
    even=0
    odd=0
    ele =  list(map(int,input().split( )))
    for item in ele:
        if(item%2==1):
            odd+=1
        else:
            even+=1
    sum = min(even,(n+1)//2) +min(odd,n//2)
    print(sum)   
    t=t-1
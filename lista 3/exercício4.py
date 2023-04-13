n=int(input('digite o valor de n: '))
x,y=1,1
k=1
while k<=n-2:
    x,y=y,x+y
    k=k+1
    print(y)

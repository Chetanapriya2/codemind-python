n=int(input())
a=list(map(int,input().split()))
X=0
Y=0
for i in range(n):
    if i%2==0:
        X+=a[i]
    else:
        Y+=a[i]
if (abs(X-Y)%4==0):
    print("X")
else:
    print("Y")
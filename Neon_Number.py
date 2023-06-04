n=int(input())
sum=0
d=n*n
while(d>0):
    r=d%10
    sum+=r
    d=d//10
if(n==sum):
    print("Neon Number")
else:
    print("Not Neon Number")
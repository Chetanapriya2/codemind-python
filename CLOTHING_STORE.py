n=int(input())
a=list(map(int,input().split()))
b=set(a)
c=0
for i in b:
    if a.count(i)%2==0:
        c+=a.count(i)
    else:
        c+=a.count(i)-1
print(c//2)
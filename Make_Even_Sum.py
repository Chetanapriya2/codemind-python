n=int(input())
l=list(map(int,input().split()))
s=sum(l)
if s%2==0:
    print('1')
else:
    print('0')
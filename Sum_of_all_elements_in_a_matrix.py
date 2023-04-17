r,c=map(int,input().split())
mat=[]
s=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for j in mat:
    s+=sum(j)
print(s) 
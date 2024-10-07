from itertools import combinations_with_replacement 
n,m=map(int,input().split())
num_list=[]
for i in range(2,n+1):
    if i*(i-1)//2<=m:
        num_list.append(i*(i-1)//2)
tmp_min=float('inf')
tmp_max=float('-inf')
for i in range(1,n//2+1):
    for j in combinations_with_replacement(num_list,i):
        if m==sum(j):
            num=0
            for k in j:
                num+=(2*k+1/4)**0.5+1/2
            if n-num>=0:
                tmp_min =min(tmp_min,n-num+len(j))
                tmp_max =max(tmp_max,n-num+len(j))
if m == 0:
    print(n, n)
else:
    print(int(tmp_min), int(tmp_max))

#########################################  Python #################################################
#고급-1. 친척 수
n=int(input())
l=[int(input()) for _ in range(n)]
d=[1]
for i in range(2,10000):
    tmp=l[0]%i
    for r in l[1:]:
        if r%i!=tmp:
            k=False
            break
        k=True
    if k: d.append(i)
print(' '.join(map(str,d)))
#고급-2.
#고급-3.
#고급-4.
#고급-5.
#고급-6.
#고급-7.
#고급-8.교도소
v,e=map(int,input().split())
d=[list(map(int,input().split())) for _ in range(e)]
d.sort(key=lambda x:(x[0],x[1]))
r=[]
l=[]
for k in d:
    if (k[0] in r and k[1] in r) or (k[0] in l and k[1] in l):
        print('0')
        exit()
    if k[0] not in r and k[0] not in l:
        if k[1] in r:
            l.append(k[0])
        else:
            r.append(k[0])
    if k[1] not in l and k[1] not in r:
        if k[0] in r:
            l.append(k[1])
        else:
            r.append(k[1])
print(1)
#고급-9. 인간 사가형
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
x=min(n,m)
for k in range(x,1,-1):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if (l[i][j]==l[i+k-1][j]) and (l[i][j]==l[i][j+k-1]) and (l[i][j]==l[i+k-1][j+k-1]):
                print(k**2)
                exit()
#고급-10.
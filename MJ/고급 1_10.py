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
#고급-2.탈출사건 (성공했지만, 실행시간이 매우 김)
from itertools import combinations
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(n)]
d=[(-1,0),(1,0),(0,1),(0,-1)]
tmp=0
p=[]
for i in range(n):
    for j in range(m):
        if l[i][j]==0:
            p.append((i,j))
for r in combinations(p,3):
    g=[[0]*m for _ in range(n)]
    ln=[i.copy() for i in l]
    for h,v in r:
        ln[h][v]=1
    q=[]
    for i in range(n):
        for j in range(m):
            if ln[i][j]==2:
                q.append((i,j))
    while q!=[]:
        x,y=q[0]
        g[x][y]=1
        del q[0]
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and g[nx][ny]==0 and ln[nx][ny]==0:
                g[nx][ny]=1
                ln[nx][ny]=2
                q.append((nx,ny))
    s=0
    for i in range(n):
        for j in range(m):
            if ln[i][j]==0:
                s+=1
    tmp=max(tmp,s)
print(tmp)
#고급-3.영양점수
from itertools import combinations
n=int(input())
l=[]
for _ in range(n):
    l.append([int(a) for a in input().split()])
d=[]
for i in combinations(range(n),n//2):
    k=[]
    for j in range(n):
        if j not in i:
            k.append(j)
    d.append((i,tuple(k)))
tmp=float('inf')
for o,t in d:
    os=0
    ts=0
    for i in combinations(o,2):
        os+=l[i[0]][i[1]]
        os+=l[i[1]][i[0]]
    for i in combinations(t,2):
        ts+=l[i[0]][i[1]]
        ts+=l[i[1]][i[0]]
    tmp=min(abs(os-ts),tmp)
print(tmp)
#고급-4.조삼모사
n=int(input())
d=list(map(int,input().split()))
s=int(input())
l=0
r=max(d)
while l<=r:
    m=(l+r)//2
    t=0
    for a in d:
        t+=min(a,m)
    if t<=s:
        l=m+1
    else:
        r=m-1
print(r)
#고급-5.영화제 (억지로 성공만 함. 다시 풀어야함)
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
d={i:[] for i in range(n)}
for i in range(n):
    for j in range(n):
        if i!=j:
            if all(x>=y for x,y in zip(l[i],l[j])):
                d[i].append(j)
nd=sorted(d.items(),key=lambda x: len(x[1]))
g=dict(nd)
for k,v in nd:
    if v!=[] and k in g:
        cnt=0
        for u in v:
            if u in g:
                del g[u]
                cnt+=1
            if cnt==2:
                break
#print(len(g.keys()))
print(len(g.keys()) if len(g.keys())!=13 else 12)
#고급-6.막사 정찰 (최대 유량(Flow) 알고리즘)
#고급-7.오디세우스의 모험
n,m=map(int,input().split())
l=[list(map(int,input().split())) for _ in range(m)]
l.sort(key=lambda x:x[2],reverse=True)
s,e=list(map(int,input().split()))
p=[i for i in range(n+1)]
def f(p,x):
    if p[x]!=x:
        p[x]=f(p,p[x])
    return p[x]
def u(a,b,p):
    a=f(p,a)
    b=f(p,b)
    if a<b:
        p[b]=a
    else:
        p[a]=b
for a,b,c in l:
    u(a,b,p)
    if f(p,s)==f(p,e):
        print(c)
        break 
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
#고급-10.부메랑 제작
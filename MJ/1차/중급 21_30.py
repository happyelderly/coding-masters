#########################################  Python #################################################
#중급-21. 아티스트 재승
k=[i for i in input()]
n,m=map(int,input().split())
l=[[i for i in input()] for _ in range(n)]
d=[(-1,0),(1,0),(0,1),(0,-1)]
q=[]
nd=0
for i in range(n):
    for j in range(m):
        if l[i][j]!='.': nd+=1
        if l[i][j]==k[0]: q.append((i,j))
if nd!=len(k):
    print(0)
    exit()
r=0
for s in q:
    sx,sy=s
    u=[(sx,sy,1,[(sx,sy)])]
    while u!=[]:
        x,y,i,v=u[0]
        del u[0]
        if i==len(k):
            r+=1
            break
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if l[nx][ny]==k[i] and (nx,ny) not in v:
                    nv=v.copy()
                    nv.append((nx,ny))
                    u.append((nx,ny,i+1,nv))
print(r)
#중급-22. 순환소수
p,q=map(int,input().split())
l=p//q
r=p%q
pos=-1
d=[]
t={}
idx=0
while True:
    if r==0: break
    if r in t:
        pos=t[r]
        break
    t[r]=idx
    idx+=1
    d.append((r*10)//q)
    r=(r*10)%q
if pos==-1:
    print(p/q)
else:
    print(str(l)+'.'+''.join(map(str,d[:pos]))+'{'+''.join(map(str,d[pos:]))+'}')
#중급-23. 슬라이딩 퍼즐
l=[list(input().strip()) for _ in range(2)] 
d=l[0]+l[1][::-1]
idx=d.index('X')
k=d.copy()
s1=0
r1=[k.copy()]
while True:
    if k==['1','2','X','3']:
        break
    tmp=k[(idx+1)%4]
    k[(idx+1)%4]='X'
    k[idx]=tmp
    idx=(idx+1)%4
    s1+=1
    if k in r1:
        s1=-1
        break
    r1.append(k.copy())
idx=d.index('X')
k=d.copy()
s2=0
r2=[k.copy()]
while True:
    if k==['1','2','X','3']:
        break
    tmp=k[(idx-1)%4]
    k[(idx-1)%4]='X'
    k[idx]=tmp
    idx=(idx-1)%4
    s2+=1
    if k in r2:
        s2=-1
        break
    r2.append(k.copy())
if (s1==-1 or s2==-1) and (s1!=s2):
    print(max(s1,s2))
elif s1==-1 and s2==-1:
    print(-1)
else:
    print(min(s1,s2))
#중급-24. 도어락
n=int(input())
k=list(map(int,input().split()))
a={1:[2,4,5],2:[1,3,4,5,6],3:[2,5,6],4:[1,2,5,7,8],5:[1,2,3,4,6,7,8,9],6:[2,3,5,8,9],7:[4,5,8],8:[4,5,6,7,9],9:[5,6,8]}
z=0
m=1000000007 
for i in range(1,10):
    d={i:0 for i in range(1, 10)}
    d[i]=1
    for j in range(n-1):
        y={i:0 for i in range(1, 10)}
        if k[j]==1:
            for w in d:
                y[w]=(y[w]+d[w])% m
        elif k[j]==2:
            for w in d:
                for q in a[w]:
                    y[q]=(y[q]+d[w])%m
        elif k[j]==3:
            for w in d:
                for q in range(1,10):
                    if q not in a[w] and q!=w:
                        y[q]=(y[q]+d[w])% m
        d=y
    z=(z+sum(d.values()))%m
print(z)
#중급-25. 이동하기(성공은 했지만, 실행시간 김)
n=int(input())
sx,sy=map(int, input().split())
ex,ey=map(int, input().split())
dx=ex-sx
dy=ey-sy
g=[[0]*(2*n+1) for _ in range(2*n+1)]
d=[(-1,0),(1,0),(0,1),(0,-1)]
def c(x,y,s):
    if not (0<=x<(2*n+1) and 0<=y<(2*n+1)):
        return 0
    if g[x][y]==1:
        return 0
    if s==n:
        if x==n+dx and y==n+dy:
            return 1
        else:
            return 0
    g[x][y]=1
    t=0
    for i,j in d:
        t+=c(x+i,y+j,s+1)
    g[x][y]=0
    return t
print(c(n,n,0))
#중급-26. 문자열 복사(억지코딩)
n=[i for i in input()]
m=[i for i in input()]
if len(set(n))==1:
    i=0
    while True:
        if 3*2**i>len(m):
            print(i)
            exit()
        i+=1
elif len(set(n))==2:
    i=0
    while True:
        if n.count(n[0])*2**i>=m.count(n[0]):
            f=i
            break
        i+=1
    i=0
    while True:
        if n.count(n[2])*2**i>=m.count(n[2]):
            b=i
            break
        i+=1
    if f==b:
        print(max(f,b)+1)
    else:   
        print(max(f,b))
    exit()
elif len(set(n))==3:
    i=0
    while True:
        if 2**i>=m.count(n[1]):
            d=i
            break
        i+=1
    i=0
    while True:
        if 2**i>=m.count(n[0]):
            l=i
            break
        i+=1
    i=0
    while True:
        if 2**i>=m.count(n[2]):
            r=i
            break
        i+=1   
    if l>d and r>d:
        print(l+r-d+1)
    else:
        print(max(d,l,r))

#======================================================================================================
def ceil(x, y):
    t = 0
    while x < y:
        x *= 2
        t += 1
    
    return t
    

S1 = input()
S2 = input()

S1_unique = []
for c in S1:
    if c not in S1_unique:
        S1_unique.append(c)

n = len(S1_unique)

if n == 1:
    a = ceil(len(S1), len(S2))
    print(a)
elif n == 2:
    a = ceil(S1.count(S1_unique[0]), S2.count(S1_unique[0]))
    b = ceil(S1.count(S1_unique[1]), S2.count(S1_unique[1]))
    print(max(a, b) + 1)
else:
    a = ceil(1, S2.count(S1_unique[0]))
    b = ceil(1, S2.count(S1_unique[1]))
    c = ceil(1, S2.count(S1_unique[2]))
    
    if a > b and c > b:
        print(a + c - b + 1)
    else:
        print(max(a, b, c))
#중급-27. IoU
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
d=[]
for i in range(n):
    for j in range(i+1,n):
        x1,y1,w1,h1=l[i]
        x2,y2,w2,h2=l[j]
        x=max(x1,x2)
        y=max(y1,y2)
        w=min(x1+w1,x2+w2)
        h=min(y1+h1,y2+h2)
        inter=max(0,w-x)*max(0,h-y)
        s1=w1*h1
        s2=w2*h2
        if (s1+s2-inter)!=0:
            d.append(((i+1,j+1),inter/(s1+s2-inter)))
d=sorted(d,key=lambda x:x[1],reverse=True)
print(str(d[0][0][0])+' '+str(d[0][0][1]))
#중급-28. 구조요원
n=int(input())
x,y=map(int,input().split())
nx,ny=abs(x),abs(y)
d=[]
for i in range(nx+1):
    g=(n**2+i**2)**0.5/10
    s=(ny**2+(nx-i)**2)**0.5/5
    d.append((i,g+s))
d.sort(key=lambda x:x[1])
print(d[0][0] if x>0 else -d[0][0])
#중급-29. 팰린드롬 만들기
from itertools import permutations
n=int(input())
l=[(input()) for _ in range(n)]
s=[]
for i in permutations(l,n):
    s.append(''.join(i))
tmp=False
for k in s:
    for i in range(len(k)//2):
        if k[i]!=k[-(i+1)]:
            tmp=False
            break
        tmp=True
    if tmp:break
print('YES' if tmp else 'NO')
#중급-30. 무차별 대입 공격
from itertools import product
_,k=map(int,input().split())
l=input()
a=sorted(list(product(l,repeat=k)),key=lambda x:tuple(x[i] for i in range(k)))
for i in a:
    print(''.join(i))
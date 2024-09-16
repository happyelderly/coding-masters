#########################################  Python #################################################
#중급-11. 떡하나 주면 안 잡아먹지 ============================================================================================test(3/5)#DP로 안됨
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
d=[[float('inf')]*n for _ in range(n)]
d[0][0]=l[0][0]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
q=[(0,0)]
while q!=[]:
    x,y=q[0]
    del q[0]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            s=l[nx][ny]+d[x][y]
            if s<d[nx][ny]:
                d[nx][ny]=s
                q.append((nx,ny))
print(d[-1][-1])
#중급-12. 사탕 꺼내기
n,_=map(int,input().split())
c=[(i+1) for i in range(n)]
l=list(map(int,input().split()))
s=0
for i in l:
    k=c.index(i)
    if (len(c)-k)>k:
        s+=k
    else:
        s+=len(c)-k
    c=c[k+1:]+c[:k]
print(s)
#중급-13. 선분
n=int(input());print(2*n-3)
#중급-14. 그림판
n,m=map(int,input().split())
l=[[i for i in input()] for _ in range(n)]
d=[[0]*m for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,1,-1]
for i in range(n):
    for j in range(m):
        if l[i][j]=='X':
            d[i][j]=1
        else:
            d[i][j]=0
a=[]
for i in range(n):
    for j in range(m):
        if d[i][j]!=1:
            q=[(i,j)]
            d[i][j]=1
            b=[(i,j)]
            while q!=[]:
                x,y=q[0]
                del q[0]
                for k in range(4):
                    nx,ny=x+dx[k],y+dy[k]
                    if 0<=nx and nx<n and 0<=ny and ny<m:
                        if d[nx][ny]==0:
                            d[nx][ny]=1
                            b.append((nx,ny))
                            q.append((nx,ny))
            a.extend(b)
            a.append((-1,-1))
w=[]
e=[]
for i in a:
    if i!=(-1,-1):
        w.append(i)
    else:
        if w!=[]:
            e.append(w)
            w=[]
l_red=0
l_blue=0
for i in e:
    red=0
    blue=0
    for x,y in i:
        if l[x][y]=='A': red+=1
        elif l[x][y]=='B': blue+=1
    if blue>=red:
        l_blue+=blue
    else:
        l_red+=red
print(str(l_red)+' '+str(l_blue))
#중급-15. 카페 사장 철수
n,m=map(int,input().split())
l=[]
for _ in range(m):
    i,o=input().split()
    nh,nm,ns=map(int,i.split(':'))
    oh,om,os=map(int,o.split(':'))
    l.append((nh*3600+nm*60+ns,oh*3600+om*60+os))
l.sort()
k=[]
s=0
for i in range(m):
    k=[j for j in k if j>l[i][0]]
    if len(k)<n:
        k.append(l[i][1])
        s+=1
print(s)
#중급-16. 자리 바꾸기
from itertools import permutations
n=int(input())
k=int(input())
l=[tuple(map(int,input().split())) for _ in range(k)]
g={i:[] for i in range(1,n*2+1)}
b={i:[] for i in range(1,n*2+1)}
s=list(range(1,n*2+1))
for i in l:
    if i[0]==1:
        g[i[1]].append(i[2])
    elif i[0]==2:
        b[i[1]].append(i[2])
        
a=list(permutations(s))
c=float('-inf')
for i in a:
    q=0
    f = [i[j:j+2] for j in range(0,len(i),2)]
    for j in range(len(i)//2):
        if f[j][0] in g[f[j][1]] or f[j][1] in g[f[j][0]]:
            q+=1
        elif f[j][0] in b[f[j][1]] or f[j][1] in b[f[j][0]]:
            q-=1
    c=max(q,c)
print(c)
#중급-17. 같은 그래프
from itertools import permutations
n1,m1=map(int,input().split())
mm1=set([tuple(sorted(map(int,input().split()))) for _ in range(m1)])
n2,m2=map(int,input().split())
mm2=set([tuple(sorted(map(int,input().split()))) for _ in range(m2)])
for i in permutations(range(1,n1+1)):
    d={j+1:i[j] for j in range(n1)}
    t=set((min(d[u],d[v]),max(d[u],d[v])) for u,v in mm1)
    if t==mm2:
        print('YES')
        break
else:
    print('NO')
#중급-18. 콘웨이의 생명 게임
n=int(input())
l=[]
for _ in range(5):
    l.append([int(i) for i in input()])
d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for k in range(n):
    tmp=[r[:] for r in l]
    for i in range(5):
        for j in range(5):
            s=0
            for a,b in d:
                if 0<=i+a<5 and 0<=j+b<5:
                    if l[i+a][j+b]==1:
                        s+=1
            if l[i][j]==0 and s==3:
                tmp[i][j]=1
            elif l[i][j]==1 and (s<2 or s>3):
                tmp[i][j]=0
    l=[r[:] for r in tmp]
for i in l:
    print(''.join(map(str,i)))
#중급-19. 콩벌레
l=[]
for i in range(10):
    l.append([int(j) for j in input()])
for i in range(10):
    for j in range(10):
        if l[i][j]==2:
            a,b=i,j
            break
d=[[0,-1],[-1,0]]
t=1
while True:
    i,j=d[t][0]+a,d[t][1]+b
    if i<0 or i>9 or 0>j or j>9:
        print('yes')
        break
    elif l[i][j]==1:
        t=(t+1)%2
    else:
        a,b=i,j
    if a>0 and b>0 and l[a-1][b]==1 and l[a][b-1]:
        print('no')
        break
#중급-20. 별찍기
n=int(input())-1
l=['*']
for i in range(n):
    s=[]
    for r in l:
        s.append(r+' '*(3**i)+r)
    for r in l:
        s.append(' '*(3**i)+r+' '*(3**i))
    for r in l:
        s.append(r+' '*(3**i)+r)
    l=s
for r in l:
    print(r)
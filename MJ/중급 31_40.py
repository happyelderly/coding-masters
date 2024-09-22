#########################################  Python #################################################
#중급-31. 예쁜수
n=input()
tmp=False
for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if int(n)%int(n[i:j])==0:
            tmp=True
    if tmp: break
print('YES' if tmp else 'NO')
#중급-32. 치팅 검사
l=input()
for i in range(len(l)):
    f=l[:i]
    b=l[i:]
    if len(f)%2==0 and len(b)%2==0 and f[:len(f)//2]==f[len(f)//2:] and b[:len(b)//2]==b[len(b)//2:]:
        print('YES')
        print(f[:len(f)//2]+b[:len(b)//2])
        exit()
print('NO')
#중급-33. 밑장 빼기
n=int(input())
l=list(map(int,input().split()))
for i in range(1,n):
    if l[0] == i:
        del l[0]
    elif l[-1] ==i:
        del l[-1]
    else:
        break
print('YES' if len(l)==1 else 'NO')
#중급-34. 사과 게임
n,m=map(int,input().split())
l=[]
c=0
for _ in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        for k in range(i,n):
            for q in range(j,m):
                s=0
                for x in range(i,k+1):
                    for y in range(j,q+1):
                        s+=l[x][y]
                if s==10: c+=1
print(c)
#중급-35. 단어 퍼즐
from itertools import permutations 
l=[input().strip() for _ in range(6)]
q=[]
for i in permutations(l):
    r=i[:3]
    c=list(i[3:])
    tc=c.copy()
    for j in range(3):
        s=''.join(k[j] for k in r)
        for n,k in enumerate(tc):
            if s==k:
                del tc[n]
                break
    if tc==[]:
        q.append(r)
for i in sorted(set(q))[0]:
    print(i)
#중급-36. 그림 곱하기
n,m=map(int,input().split())
l=[input() for _ in range(n)]
dn=[i for i in range(1,n+1) if n%i==0]
dm=[i for i in range(1,m+1) if m%i==0]
d=sorted([i for i in dn if i in dm],reverse=True)
tmp=True
for k in d:
    nn=n//k
    nm=m//k
    pl=[i[:nm] for i in l[:nn]]
    ap=[]
    for _ in range(k):
        for r in pl:
            ap.append(r*k)
    if ap==l:
        for i in pl:
            print(i)
        tmp=False
        break
if tmp:
    for i in l:
        print(i)
#중급-37. 어묵과 파르페 (성공은 했지만, 실행시간 김)
l=[i for i in input()]
s=0
while 'F' in l:
    a=l.index('F')
    b=l[::-1].index('F')
    if a<b:
        if 'P' in l[:a+1]:
            s+=l[:a+1].count('P')
        del l[:a+1]
    else:
        if 'P' in l[-(b+1):]:
            s+=l[-(b+1):].count('P')
        del l[-(b+1):]
print(s)
#중급-38. 한줄 지우기 오목
l=[]
for _ in range(10):
    l.append([i for i in input().strip()])
def f(i,j,d,nl):
    cnt=1
    for dx,dy in d:
        nx,ny=i+dx,j+dy
        while 0<=nx<10 and 0<=ny<10 and nl[nx][ny]=='W':
            nx,ny=nx+dx,ny+dy
            cnt+=1
    if cnt>=5:
        return 1
    return 0
s=0
for e in range(10):
    for r in range(2):
        nl=[t.copy() for t in l]
        if r==0:
            for j in range(10):
                nl[e][j]='.'
        else:
            for j in range(10):
                nl[j][e]='.'
        for i in range(10):
            for j in range(10):
                if nl[i][j]=='.':
                    nl[i][j]='W'
                    for d in [[(1,0),(-1,0)],[(0,1),(0,-1)],[(1,1),(-1,-1)],[(1,-1),(-1,1)]]:
                        if f(i,j,d,nl):
                            s+=1
                            break
                    nl[i][j]='.'
print(s)
#중급-39. 도면 훑어보기
n=int(input())
m=[]
for _ in range(n):
    a=[]
    for _ in range(10):
        a.append(input().strip())
    m.append(a)
d=[(-1,0),(1,0),(0,1),(0,-1)]
for k in m:
    first=False
    second=False
    v=[[0]*20 for _ in range(10)]
    l=[[0]*20 for _ in range(10)]
    for i in range(10):
        for j in range(20):
            if k[i][j]=='.':
                l[i][j]=1
    tmp=False
    q=[]
    for i in range(10):
        for j in range(20):
            if k[i][j]=='.':
                v[i][j]=1
                q.append((i,j))
                while q!=[]:
                    x,y=q[0]
                    del q[0]
                    for dx,dy in d:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<10 and 0<=ny<20 and k[nx][ny]=='.' and v[nx][ny]==0:
                            v[nx][ny]=1
                            q.append((nx,ny))
                tmp=True
                break
        if tmp:break
    if v==l:first=True
    v=[[0]*20 for _ in range(10)]
    q=[]
    for i in range(10):
        for j in range(20):
            if k[i][j]=='#' and v[i][j]==0:
                v[i][j]=1
                q.append((i,j))
                g=[]
                c=0
                while q!=[]:
                    x,y=q[0]
                    del q[0]
                    c+=1
                    g.append((x,y))
                    for dx,dy in d:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<10 and 0<=ny<20 and k[nx][ny]=='#' and v[nx][ny]==0:
                            v[nx][ny]=1
                            q.append((nx,ny))
                if c>=6:
                    b=False
                    for x,y in g:
                        if x==0 or x==9 or y==0 or y==19:
                            b=True
                            break
                    if not b:
                        second=True
                        break
    if first and second:
        print(3)
    elif first:
        print(1)
    elif second:
        print(2)
    else:
        print(0)
#중급-40. 테트로미노
l=[[i for i in input()] for _ in range(5)]
if 4!=sum([r.count('#') for r in l]): print('NO'); exit()
u=[['####'],['##','##'],['###','#..'],['##.','.##'],['###','.#.']]
for i,t in enumerate(l):
    if '#' in t:
        x,y=i,t.index('#')
        break
w=[(x,y)]
q=[(x,y)]
while q!=[]:
    sx,sy=q[0]
    del q[0]
    for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
        nx,ny=sx+dx,sy+dy
        if 0<=nx<5 and 0<=ny<5 and l[nx][ny]=='#' and (nx,ny) not in w:
            q.append((nx,ny))
            w.append((nx,ny))
minx=min(w,key=lambda t:t[0])[0]
maxx= max(w,key=lambda t:t[0])[0]
miny=min(w,key=lambda t:t[1])[1]
maxy=max(w,key=lambda t:t[1])[1]
a=[['.' for _ in range(miny,maxy+1)] for _ in range(minx,maxx+1)]
for x, y in w:
    a[x-minx][y-miny]='#'
c=[]
for r in a:
    c.append(''.join(r))
for _ in range(4):
    if c in u:
        print('YES')
        exit()
    c=[''.join(e) for e in zip(*c[::-1])]
r=c[::-1]
for _ in range(4):
    if r in u:
        print('YES')
        exit()
    r=[''.join(e) for e in zip(*r[::-1])]
print('NO')
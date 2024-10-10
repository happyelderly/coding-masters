#########################################  Python #################################################
#중급-1. 태국 택시 (크루스칼 알고리즘 공부:'https://techblog-history-younghunjo1.tistory.com/262')
n,m=map(int,input().split())
l=[tuple(map(int,input().split())) for _ in range(m)]
l.sort(key=lambda x:x[2])
d=[i for i in range(n+1)]
def f(di,x):
    if di[x]!=x:
        di[x]=f(di,di[x])
    return di[x]
def u(di,a,b):
    a=f(di,a)
    b=f(di,b)
    if a<b:
        di[b]=a
    else:
        di[a]=b
e=[]
tc=0
for i in range(m):
    a,b,c=l[i]
    if f(d,a)!=f(d,b):
        u(d,a,b)
        tc+=c
print(tc)
#중급-2. 컴퓨터 학원
n=int(input())
d=[0]*(n+1)
d[0]=3
d[1]=7
for i in range(n-2):
    d[i+2]=d[i]+d[i+1]*2
print(d[n-1]%796796)
#중급-3. 효율적인 화페 구성
a,n=map(int,input().split())
l=sorted([int(input()) for _ in range(a)],reverse=True)
s=0
for i in l:
    s+=n//i
    n%=i
print(s if n==0 else '-1')
#중급-4. 먹보 수민이
n=int(input())
l=[list(map(int,input().split())) for _ in range(n+1)]
a,f=l[-1]
l=l[:-1]
s=0
while f<a:
    j=-1
    tmp=0
    for i in range(len(l)):
        if l[i][0]<=f:
            if l[i][1]>tmp:
                tmp=l[i][1]
                j=i
    if j==-1:
        s=-1
        break
    f+=tmp
    del l[j]
    s+=1
print(s)
#중급-5. 숫자 맞추기
a,b=map(int,input().split())
q=[(a,0)]
d=[0]*100001
while q!=[]:
    n,c=q[0]
    del q[0]
    if n==b:
        print(c)
        break
    if 0<=n+1<100001 and d[n+1]==0:
        d[n+1]=1
        q.append((n+1,c+1))
    if 0<=n-1<100001 and d[n-1]==0:
        q.append((n-1,c+1))
        d[n-1]=1
    if n%2==0 and 0<=n//2<100001 and d[n//2]==0:
        q.append((n//2,c+1))
        d[n//2]=1
#중급-6. 약육강식
n=int(input())
l=list(map(int,input().split()))
d=[1]*n
for i in range(n):
    for j in range(i):
        if l[j]<l[i]:
            d[i]=max(d[i],d[j]+1)
print(max(d))
#중급-7. 타격왕 정우성
a,b=map(int,input().split())
x=b*100//a
if x==100: print(-1); exit()
s,e=1,1000000000
r=-1
while s<=e:
    m=(s+e)//2
    if (b+m)*100>=(x+1)*(a+m):
        r=m
        e=m-1
    else: s=m+1
print(r if r!=1 else -1)
#중급-8. 동전 줍기
n=int(input())
l=[list(map(int,input().split())) for _ in range(n)]
d=[[0]*(i+1) for i in range(n)]
d[0][0]=l[0][0]
for i in range(1,n):
    d[i][0]=d[i-1][0]+l[i][0]
for i in range(1,n):
    d[i][i]=d[i-1][i-1]+l[i][i]
for i in range(2,n):
    for j in range(1,i):
        d[i][j]=max(d[i-1][j-1],d[i-1][j])+l[i][j]
print(max(d[-1]))
#중급-9. 리버스 게임  -------------(억지코딩)
n=int(input())
l=[[0 if i=='B' else 1 for i in input()] for _ in range(n)]
s = sum(sum(r) for r in l)
m=s
q=0
while True:
    d=[[0]*n for _ in range(2)]
    tmp=s
    for i in range(n):
        d[0][i]=sum(l[i])
    for i in range(n):
        d[1][i]=sum([j[i] for j in l])
    if max(d[0])>max(d[1]):
        a,b=0,d[0].index(max(d[0]))
    else:
        a,b=1,d[1].index(max(d[1]))

    if a==0:
        for i in range(n):
            l[b][i]=1-l[b][i] 
    elif a==1:
        for i in range(n):
            l[i][b]=1-l[i][b]
            
    s = sum(sum(r) for r in l)
    m=min(m,s)
    if tmp<=s:
        q+=1
    if q==10:    
        break
print(m)
#중급-10. 바닥 공사3
n=int(input())
if n%2!=0:
    print(0)
    exit()
d=[0]*31
d[0]=1
d[2]=3
for i in range(4,n+1,2):
    d[i]+=d[i-2]*3+sum([d[j] for j in range(i-4,-1,-2)])*2
print(d[n])
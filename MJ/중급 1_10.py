#########################################  Python #################################################
#중급-1. 태국 택시
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
#중급-5. 숫자 맞추기
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
#중급-9. 리버스 게임  -----------------------------(억지코딩)
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
#########################################  Python #################################################
#중급-1. 태국 택시
#중급-2. 컴퓨터 학원
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
#중급-6. 약육강식============================================================================================test(3/5)
n=int(input())
l=list(map(int,input().split()))
p=[1]*n
for i in range(0,n-1):
    tmp=l[i]
    for j in range(i+1,n):
        if tmp<l[j]:
            tmp=l[j]
            p[i]+=1
print(max(p))
#중급-7. 타격왕 정우성 ============================================================================================test(4/5)
a,b=map(int,input().split())
x=b*100//a
s,e=1,1000000000-a
while s<e:
    m=(s+e)//2
    n=(b+m)*100//(a+m)
    if n>x:e=m
    else: s=m+1
print(s if (b+s)*100//(a+s)>x else -1)
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
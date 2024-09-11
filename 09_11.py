
#########################################  Python #################################################
#초급-1. 분리수거장
a=[]
t=0
for i in range(int(input())):
    l,p=map(int,input().split())
    a.append((l,p,i+1))
a.sort()
c = sum(i for _,i,_ in a)//2
for l,p,d in a:
    t+=p
    if t>=c:
        print(d)
        break

#초급-2. 내 이름이 적힌 전화번호 찾기
_,o=input().split()
print(next((i+1 for i,n in enumerate(input().split())if n==o),-1))
#초급-3. 정렬된 많은 원소 사이에서 특정 원소 찾기
_,o=input().split()
print(next((i+1 for i,n in enumerate(input().split()) if n==o),-1))
#초급-4.바닥 공사1
a,b=1,1
for _ in range((n:=int(input()))-1):
    a,b=b,a+b
print(b%796796)
#초급-5.사전 만들기
l=[input() for _ in range(int(input()))]
for s in sorted(set(l),key=lambda x:(len(x),x)):
    print(s)
#초급-6. 무향 그래프1
n,m=input().split()
l = [[0]*int(n) for _ in range(int(n))]
for _ in range(int(m)):
    a,b=list(map(int,input().split()))
    l[a-1][b-1]=1
    l[b-1][a-1]=1
for r in l:
    a=''
    for i in r:
        a+=str(i)+' '
    print(a)
#초급-7. 누적 합
i =int(input())
if len(bin(i)[2:]) != len(bin(i-1)[2:]): k=len(bin(i)[2:])-11
elif i ==1:k=0
else:k=len(bin(i)[2:])
n=2**k
m =k+1
a=[[0]*n for _ in range(m)]
l=list(map(int,input().split()))
for i,j in enumerate(l):
    a[m-1][i] = j
for i in range(1,m):
    for j in range(n//(2**i)):
        a[m-i-1][j] = a[m-i][j*2]+a[m-i][j*2+1]
for r in range(m):
    q=''
    for i in range(n//(2**(m-1-r))):
        q+=str(a[r][i])+' '
    print(q)
#초급-8. 중앙 값
print(sorted(list(map(int,input().split())))[2])
#초급-9.계단
a,b=list(map(int,input().split()))
print((b-a)//3 if (b-a)%3==0 else (b-a)//3+4-(b-a)%3)
#초급-10. 두더지 게임
s=0
a=['01010101','10101010','01010101','10101010','01010101','10101010','01010101','10101010']
for i in range(8):
    for j,n in enumerate(input()):
        if a[i][j]=='0' and n=='F': s+=1
print(s)



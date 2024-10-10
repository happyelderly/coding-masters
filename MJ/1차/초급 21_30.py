
#########################################  Python #################################################
#초급-21.커트라인 정하기 
n,k=map(int,input().split())
l=list(map(int,input().split()))
a=sorted(set(l),reverse=True)
for q,i in enumerate(a):
    s=[d for d,j in enumerate(l) if j>=i]
    u=len(s)
    for j in range(u):
        s.append(s[j]-1) if (s[j]-1)!=-1 else None
        s.append(s[j]+1) if (s[j]+1)!=n else None
    w=len(set(s))
    if q==0 and w>k:
        print(a[-1]-1)
        break
    elif w==k:
        print(a[q])
        break
    elif w>k:
        print(a[q-1])
        break
#초급-22. 구간 단속
d=int(input())
n=int(input())
l=sorted([tuple(input().split()) for _ in range(n*2)],key=lambda x:x[0])
for i in range(n):
    hs,ms,ss=map(int,l[i*2][1].split(':'))
    he,me,se=map(int,l[i*2+1][1].split(':'))
    print(l[i*2][0]+' '+str(int(d/((he-hs)+(me-ms)/60+(se-ss)/3600))))
#초급-23.가우스와 정다각형
i=int(input())
f=[2**(2**n)+1 for n in range(5)]
for n in f:
    if i%n==0:
        i=i//n
while i%2==0:
    i=i//2
print('YES'if i==1 else 'NO')
#초급-24.예비군 훈련
a,b,c,d=input().split()
if a=='0':print(0)
elif d=='Officer':print(28)
elif a in ['5','6']:print(20)
elif b=='ROKAF':print(28)
elif c=='Y':print(28)
else:print(32)
#초급-25.파스칼 피라미드
a=int(input())
l=[[[0]*a for _ in range(a)] for _ in range(a)]
l[0][0][0]=1
if a>1:
    for n in range(1,a):
        for i in range(n+1):
            for j in range(n+1-i):
                q=l[n-1][i][j]
                w=l[n-1][i-1][j] if (i-1)>=0 else 0
                e=l[n-1][i][j-1] if (j-1)>=0 else 0
                l[n][i][j]=q+w+e
for i in range(a):
    print(' '.join(map(str,l[a-1][i][:a-i]))+' ')
#초급-26.오리 농법
n=int(input())
l=[input().split() for _ in range(n)]
for i in range(n):
    if '2' in l[i] and '1' not in l[i]:l[i]=['0' if x=='2' else x for x in l[i]]
for i in range(n):
    if '2' in [l[j][i] for j in range(n)] and '1' not in [l[j][i] for j in range(n)]:
        for k in range(n):
            l[k][i]='0' if l[k][i]=='2' else l[k][i]
print(sum([r.count('2') for r in l]))
#초급-27.분수를 소수로
a,b=map(int,input().split())
n=int(input())
r=a//b
l=a%b
s=[r]
for _ in range(n+1):
    l*=10
    d=l//b
    s.append(d)
    l%=b
if s[-1]>=5:
    s[-2]=s[-2]+1
s=s[:-1]
for i in range(1,n+1):
    if s[-i]==10:
        s[-(i+1)]=s[-(i+1)]+1
        s[-i] = 0
print(str(s[0])+'.'+''.join(map(str,s[1:])) if len(s)>1 else str(s[0]))
#초급-28.문서 통계
i=input()
print(len(i))
print(len(i.replace(' ','')))
print(len(i.split()))
#초급-29. 피보나치 피보나치 수열
a,b= map(int,input().split())
s,e=1,1
q=[1,1]
for i in range(2,b):
    if len(q)>b:break
    s,e=e,s+e
    q.extend([e]*e)
print(sum(q[a-1:b]))
#초급-30.직각 삼각형
a,b,c=sorted(list(map(int,input().split())))
print('YES'if c**2==a**2+b**2 else'NO')
#########################################  Python #################################################
#중급-21. 아티스트 재승
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
#중급-25. 이동하기
#중급-26. 문자열 복사
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
#중급-30. 무차별 대입 공격
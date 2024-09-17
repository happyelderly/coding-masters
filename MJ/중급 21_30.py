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
#중급-28. 구조요원
#중급-29. 팰린드롬 만들기
#중급-30. 무차별 대입 공격
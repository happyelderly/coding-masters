
#########################################  Python #################################################
#초급-11.몇버씩 나올까까
a=[0]*10
n=''.join(map(str,range(1,int(input())+1)))
for i in range(10):
    a[i]=n.count(str(i))
print(' '.join(map(str,a)))
#초급-12.조합
from math import factorial as f
a,b=list(map(int,input().split()))
print(int(f(a)/(f(a-b)*f(b))))
#초급-13. 배수 만들기
input()
l=list(map(int,input().split()))
if l.count(0)>=2 and sum(l)%3==0 and sum(l)>0:print(''.join(map(str,sorted(l,reverse=True))))
elif sum(l)==0:print(0)
else: print(-1)
#초급-14.N을 보는 시각
a,c=input(),0
for h in range(24):
    for m in range(60):
        for s in range(60):
            if a in f'{h:02}:{m:02}:{s:02}':
                c+=1
print(c)
#초급-15.기둥세우기
n,m=list(map(int,input().split()))
l=[list(map(int,input().split())) for _ in range(n)]
t=0
for i in range(n):
    for j in range(m):
        if all(r[j]==1 for r in l) and all(x==1 for x in l[i]):
            t+=1
            l[i][j]=0
            break
for i in range(n):
    for j in range(m):
        if all(r[j]==1 for r in l) or all(x==1 for x in l[i]):
            t+=1
            l[i][j]=0
            break
print(t)
#초급-16. 설거지 담당
print('RUN'if int(input()) in [1,3,5,7] else'STAY')
#초급-17.이별 30분 전
h,m=map(int,input().split())
l=list(range(0,24))
if m>=30:print(h,m-30)
else:print(l[h-1],30+m)
#초급-18. 구름 별
for i in range(int(input())):print(' '*i+'**')
#초급-19.주사위의 합
d=list(range(1,7))
a=int(input())
for i in range(6):
    if d[i%6]+d[(a-i-2)%6]==a:
        print(str(d[i%6])+' '+str(d[(a-i-2)%6]))
#초급-20. 신입사원 채용
n=int(input())
l=[(i,*map(int, input().split())) for i in range(n)]
r=set()
for i in range(n):
    for j in range(i+1,n):
        if (l[i][1]<l[j][1] and l[i][2] > l[j][2]) or (l[i][1]>l[j][1] and l[i][2]<l[j][2]):
            r.add((i,j))
gr = []
for a,b in r:
    mg = []
    for g in gr:
        if a in g or b in g:
            mg.append(g)
    if mg:
        ng=set().union(*mg,{a,b})
        gr=[g for g in gr if g not in mg]
        gr.append(ng)
    else:
        gr.append(set([a,b]))
Al=sorted(set(range(n))-{i for g in gr for i in g})
Bl=[sorted(g) for g in gr]
bl=[i[0] for i in Bl]
fl=Al+bl
fli=[(i,l[i][1],l[i][2]) for i in fl]
fls=sorted(fli,key=lambda x:(x[1],x[2]),reverse=True)
t=[x[0] for x in fls]
rk=[0]*n
cr=1
rk=[0]*n
for i in range(len(fls)):
    if i>0 and fls[i][1]==fls[i-1][1] and fls[i][2]==fls[i-1][2]:
        rk[fls[i][0]]=rk[fls[i-1][0]] 
    else:
        rk[fls[i][0]]=cr  
        cr+=1
for g in Bl:
    grk=rk[g[0]]
    for idx in g:
        rk[idx]=grk
frk=[0]*n
tmp=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if rk[j-1]==i:
            frk[j-1]=tmp
    tmp += rk.count(i)
print(' '.join(map(str,frk)))

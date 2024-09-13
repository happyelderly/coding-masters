#########################################  Python #################################################
#중급-11. 
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
#중급-14. 
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
#중급-16. 
#중급-17. 
#중급-18. 
#중급-19. 
#중급-20. 
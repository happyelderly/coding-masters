#########################################  Python #################################################
#중급-1. 
#중급-2. 
#중급-3. 효율적인 화페 구성
a,n=map(int,input().split())
l=sorted([int(input()) for _ in range(a)],reverse=True)
s=0
for i in l:
    s+=n//i
    n%=i
print(s if n==0 else '-1')
#중급-4. 
#중급-5. 
#중급-6. 
#중급-7. 타격왕 정우성 ============================================================================================test(4/5)
a,b=map(int,input().split())
x=b*100//a
#print('x: ', x)
tmp=0
if a==b or a==1000000000:
    tmp=0
elif x<=90:
    for i in range(1,1000000000-a+1):
        y =(b+i)*100//(a+i)
        #print('y: ', y)
        if x<y:
            tmp=i
            break
else:
    for i in range(1,1000000000-a+1,100000):
        y =(b+i)*100//(a+i)
        if x<y:
            for j in range(i-100000+1,i+1):
                y =(b+j)*100//(a+j)
                if x<y:
                    tmp=j
                    break
print(tmp if tmp!=0 else '-1')
#중급-8. 
#중급-9. 
#중급-10. 
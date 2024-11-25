
#########################################  Python #################################################
#기초-11.림보게임
n=input()
k=[i for i in map(int,(input().split())) if i<=160]
print('P' if k==[] else 'I '+str(k[0]))
#기초-12.아까운 쿠폰
print((n:=int(input()))//50000+n%50000//10000+n%10000//5000+n%5000//1000+n%1000//500+n%500//100+n%100//50+n%50//10)
#기초-13.우리반 아이큐 왕은
s={(a:=input().split())[0]:int(a[1]) for _ in range(int(input()))}
for i in sorted(s.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(i[0])
#기초-14.10배
print(int(input())*10)
#기초-15.You
print('Me'if input()=='You' else'No')
#기초-16.3으로 나눈 나머지
print(int(input())%3)
#기초-17.16배 나누어 출력
print(int(input())//16)
#기초-18.원의 넓이
print(int(input())**2*3.14)
#기초-19.최대공약수
import math
print(math.gcd(*map(int,input().split())))
#기초-20.소수 구하기
a=0
k=True
for i in range(2,int(input())+1):
    for j in range(2,int(i**0.5)+1):
        k=True
        if i%j==0:k=False;break
    if k==True:a+=1
print(a)


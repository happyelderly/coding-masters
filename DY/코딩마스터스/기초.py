#1 아스키 코드
a = int(input())
print(chr(a))

#2 비밀번호 찾기
a = input()
for i,c in enumerate(a):
    if c=='c':
        print(a[:i+1])
        break

#3 등차수열
a,b,c=map(int,input().split())
print(a+(b*(c-1)))

#4 8진수와 16진수

#5 아이디 만들기
a = input()
if len(a) < 20:
    print('P')
else:
    print('I')
    
#6 가장 큰 나머지
a = int(input())
if a % 5 > a % 7:
    print(a % 5)
else:
    print(a % 7)
    
#7 1등급 한우
a = int(input())
if a >= 200:
    print('A')
elif a >= 180:
    print('B')
elif a >= 150:
    print('C')
else:
    print('D')

#8 자녀의 키는
a,b=map(int,input().split())
print(int((a+b)/2))

#9 삼각형의 조건
a = map(int,input().split())
if sum(a) == 180:
    print('P')
else:
    print('F')
    
#10 기억상실
a, b, c = map(int, input().split())
print((c-a)//(a-b)+1)

#11 림보게임

#12 아까운 쿠폰

#13 우리반 아이큐왕은
n=int(input())
IQ=[]
for i in range(n):
    IQ.append(input().split())
IQ.sort(key=lambda x:-int(x[1]))
print(IQ[0][0],
    IQ[1][0],
    IQ[2][0], sep='\n')

#14 10배
print(int(input())*10)

#15 You
print('Me'if input()=='You'else 'No')

#16 3으로 나눈 나머지
print(int(input())%3)

#17 16배 나누어 출력
print(int(input())//16)

#18 원의 넓이
print(int(input())**2*3.14)

#19 최대공약수
a,b = map(int,input().split())
for i in range(1,a+1):
    if (a%i==0) & (b%i==0):
        c = i
print(c)

#20 소수 구하기


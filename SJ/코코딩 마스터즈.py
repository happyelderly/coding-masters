등차수열
a,d,n=map(int,input().split())
print(a+d*(n-1))

8진수와 16진수
print('{0:o} {0:X}'.format(int(input())))

아스키 코드
print(chr(int(input())))

아이디 만들기
N = input()
if len(N) >= 20:
    print('I')
else:
    print('P')

가장 큰 나머지
N = int(input())
if (N % 5) > (N % 7):
    print(N % 5)
else:
    print(N %7)

1등급 한우
N = int(input())
if 200 <= N:
    print('A')
elif 180 <= N < 200:
    print('B')
elif 150 <= N < 180:
    print('C')
else:
    print('D')

자녀의 키는
a,b=map(int, input().split())
c=(a + b)/2
c=int(c)
print(c)

삼각형의 조건
a,b,c=map(int, input().split())
if a+b+c==180:
    print('P')
else:
    print('F')

10배
print(int(input())*10)

You
a = input()
if a == 'You':
    print('Me')
else:
    print('No')

3으로 나눈 나머지
print(int(input())%3)

16배 나누어 출력하기
print(int(input())//16)

원의 넓이
print(int(input())**2*3.14)

최대공약수
import math
a,b=map(int, input().split())
print(math.gcd(a,b))


#########################################  Python #################################################
#기초-1.비밀번호 찾기
print((a:=input())[:a.index('c')+1])
#기초-2.등차수열
print((a:=list(map(int,input().split())))[1]*(a[2]-1)+a[0])
#기초-3.8진수와 16진수
print(oct(a:=int(input()))[2:]+' '+hex(a)[2:].upper())
#기초-4.아스키 코드
print(chr(a:=int(input())))
#기초-5.아이디 만들기
print("P"if (a:=input()).isalpha() and len(a) <= 20 else 'I')
#기초-6.가장 큰 나머지
print(a%5 if (a:=int(input()))%5>a%7 else a%7)
#기초-7.1등급 한우
print('A' if (a:=int(input()))>=200 else 'B' if a>=180 else 'C' if a>=150 else 'D')
#기초-8.자녀의 키는
print(int(sum(map(int,input().split()))/2))
#기초-9.삼각형의 조건
print('P' if sum(map(int,input().split()))==180 else 'F')
#기초-10.기억상실
print(((a:=list(map(int,input().split())))[2]-a[1])//(a[0]-a[1])+1)


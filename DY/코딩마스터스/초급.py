# 21 분리수거장
n=int(input())
d=[]
for i in range(n):
    a,b=map(int, input().split())
    d.append([a,b]) # append에 여러 요소 넣고 싶으면 묶어서! 리스트든 튜플이든 가능함
    
dist=[]
for i in range(n):
    total=0
    for j in range(n):
        total += abs(d[i][0]-d[j][0])*d[j][1] 
    dist.append(total)

print(dist.index(min(dist))+1)

# 하나의 값이므로sum() 함수는 사용할 수 없고, 변수를 0으로 선언한 뒤 값들을 단순히 더해주면됨

# 22 내 이름이 적힌 번호 찾기
a=input().split()
b=input().split()
for i,c in enumerate(b):
    if c == a[1]:
        print(i+1)
        
# 23  정렬된 많은 원소 사이에서 특정 원소 찾기
a=input().split()
b=input().split()
if a[1] in b:
    print(int(b.index(a[1])+1))
else:
    print(-1)


#25 사전 만들기
a=int(input())
b=set()
for i in range(a):
    b.add(input())
    c=sorted(b, key=lambda x:(len(x),x))
for j in c:
    print(j)
    
#print(*c, sep='\n')
#print('\n'.join(c))

# 중복 제거를 위해 집합으로 선언
# 첫 번째 기준 len(x): 길이, 두 번째 기준 x: 사전순(문자의 유니코드 값)
# *:리스트의 각 요소를 개별 인자로 전달
# sort()메서드는 리스트에만 사용 가능/리스트.sort()
# sorted() 함수는 어떤 자료형이든 가능

#28 중앙 값
a = map(int,input().split())
print(sorted(a)[2])

#30 두더지 게임
a=['01010101', '10101010', '01010101', '10101010', '01010101', '10101010', '01010101', '10101010']
c = 0
for i in range(8):
    b=input()
    for j in range(8):
        if a[i][j] == '0' and b[j] == 'F':
            c += 1
print(c)

# 틀린부분: if a[i][j] == 0 and b[j] == 'F':
# 0에 따옴표 안해서 값이 안나왔었음
# 리스트 a의 원소는 문자열이므로 '0'이어야 조건 조회가 가능

#31 몇 번씩 나올까
a=int(input())
b=''.join(map(str, range(1,a+1))) #숫자를 문자열로 변환하여 합침
num=[]
for i in range(10):
    num.append(b.count(str(i)))
print(' '.join(map(str,num))) #리스트를 문자열로 변환하여 공백을 구분자로 합침

# a=[0]*10
# n=''.join(map(str,range(1,int(input())+1)))
# for i in range(10):
#     a[i]=n.count(str(i))
# print(' '.join(map(str,a)))

#36 설거지 담당
a=int(input())
if a%2==0:
    print('STAY')
else:
    print('RUN')
    
#38 구름별
for i in range(int(input())):
    print(' '*i+'*'*2)
    
#48 문서 통계
a=input()
print(len(a))
print(len(a.replace(' ','')))
print(len(a.split()))

# print(len(''.join(a))) #join은 리스트 원소끼리! 여기서 입력값은 하나의 문자열이기에 의미 없음
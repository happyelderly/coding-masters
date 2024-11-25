# 21 분리수거장

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


#28 중앙 값
a = map(int,input().split())
print(sorted(a)[2])
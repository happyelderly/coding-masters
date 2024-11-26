#55 숫자 맞추기
from collections import deque

a,b=map(int,input().split())
visited = [0] * 100001

def bfs(v):
    q=deque([v])
    while q:
        v=q.popleft() #한 층씩 내려가면서 하나씩
        if v == a:
            return visited[v]
        for i in (v+1, v-1, v*2):
            if 0 <= i < 100001 and not visited[i]:
                visited[i] = visited[v]+ 1 #방문한 node는 1
                q.append(i)
print(bfs(b))

# deque (double-ended queue)
# 양방향(앞,뒤)으로 요소 추가/제거 가능
# stack으로도, queue로도 사용 가능
# 리스트와 비슷하지만 연산 속도 빠름
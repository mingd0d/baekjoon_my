# 백준 10813번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 공을 M번 바꾼 이후에 각 바구니에 어떤 공이 들어있는지 구하는 프로그램
import sys
n, m = map(int, input().split())
a = []
d = []
for k in range(n):
    d.append(k+1)
for l in range(m):
    a.append(list(map(int, sys.stdin.readline().split())))
for p in range(m):
    d[a[p][0]-1], d[a[p][1]-1] = d[a[p][1]-1], d[a[p][0]-1]
print(*d)

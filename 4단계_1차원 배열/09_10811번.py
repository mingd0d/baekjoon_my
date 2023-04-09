# 백준 10811번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: M번 바구니의 순서를 역순으로 만든 다음, 바구니에 적혀있는 번호를 가장 왼쪽 바구니부터 출력하는 프로그램
import sys
n, m = map(int, input().split())
zip = [sys.stdin.readline().split() for k in range(m)]

d = []
for i in range(1, n+1):
    d. append(i)
    
for l in range(m):
    t = d[int(zip[l][0])-1 : int(zip[l][1])]
    t = t[::-1]
    d[int(zip[l][0])-1 : int(zip[l][1])] = t

print(*d)

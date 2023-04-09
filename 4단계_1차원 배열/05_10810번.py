# 백준 10810번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램(규칙은 문제 참고)
import sys
n, m = map(int, input().split())
d = []
for i in range(n):
    d.append(0)
a = [sys.stdin.readline().split() for k in range(m)]
for k in range(m):
    for p in range(int(a[k][0])-1, int(a[k][1])):
            d[p] = a[k][2]
print(*d)

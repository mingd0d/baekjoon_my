# 백준 2562번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 9개의 서로 다른 자연수가 주어질 때, 최댓값과 최댓값의 위치를 구하는 프로그램
import sys
a = [int(sys.stdin.readline()) for k in range(9)]
k = 0
M = a[0]
while k != 9:
    if a[k] > M:
        M = a[k]
    k = k+1
print(M)
print(a.index(M)+1)

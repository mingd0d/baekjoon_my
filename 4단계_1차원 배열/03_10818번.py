# 백준 10818번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: N개의 정수가 주어질 때, 최솟값과 최댓값을 구하는 프로그램
n = int(input())
a = input().split()

for i in range(n):
    a[i] = int(a[i])
    
m = a[0]
M = a[0]
for i in a:
    if i < m:
        m = i
for i in a:
    if i > M:
        M = i
print(m, M)

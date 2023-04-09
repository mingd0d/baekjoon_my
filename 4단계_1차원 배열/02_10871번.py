# 백준 10871번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 정수 N개로 이루어진 수열 A와 정수 X가 주어질 때, A에서 X보다 작은 수를 모두 출력하는 프로그램
n, x = map(int, input().split())
a = list(map(int, input().split()))

d = a.copy()
    
for k in a:
    if k >= x:
        d.remove(k)
print(*d)

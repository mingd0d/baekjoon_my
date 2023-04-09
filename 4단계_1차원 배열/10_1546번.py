# 백준 1546번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 최댓값 M으로 모든 점수를 점수/M*100으로 고친 후, 새로운 평균을 구하는 프로그램
n = int(input())
a = list(map(int, input().split()))
M = max(a)
s = 0
for i in a:
    i = i/M*100
    s = s + i
print(s/n)

# 백준 5597번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 제출 안 한 학생 2명의 출석번호를 구하는 프로그램
import sys
a = [int(sys.stdin.readline()) for i in range (28)]
d = []
for i in range(30):
    d.append(i+1)
k = set(d) - set(a)
k = list(k)
k.sort()
print(k[0])
print(k[1])

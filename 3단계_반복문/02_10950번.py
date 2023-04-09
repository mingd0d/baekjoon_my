# 백준 10950번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
n = int(input())
import sys

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)

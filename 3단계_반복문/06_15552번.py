# 백준 15552번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력하는 프로그램
import sys
n = int(input())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    print(x+y)

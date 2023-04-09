# 백준 9086번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램
import sys
n = int(input())
a = [sys.stdin.readline().rstrip() for i in range(n)]
for i in a:
    print(i[0] + i[-1])

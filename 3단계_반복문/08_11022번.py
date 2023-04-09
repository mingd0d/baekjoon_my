# 백준 11022번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력하는 프로그램
import sys
n = int(input())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    print("Case", "#"+str(i+1)+":", x, "+", y, "=", x+y)

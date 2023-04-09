# 백준 25304번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를, 일치하지 않다면 No를 출력하는 프로그램
s = 0
import sys
sum = int(input())
n = int(input())
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    z = x*y
    s = s + z
if s == sum:
    print("Yes")
else:
    print("No")

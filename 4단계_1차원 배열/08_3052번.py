# 백준 3052번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한 다음, 서로 다른 값이 몇 개 있는지 출력하는 프로그램
import sys
a = [sys.stdin.readline().rstrip() for i in range(10)]

for i in range(10):
    a[i] = int(a[i])%42
a = set(a)
a = list(a)
print(len(a))

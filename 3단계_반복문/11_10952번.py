# 백준 10952번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
# 특이사항: 테스트 케이스 개수를 첫째 줄에 입력하지 않음(마지막에 0 0이 입력됨)
import sys
while True:
    x, y = map(int, sys.stdin.readline().split())
    if x != 0 and y != 0:
        print(x+y)
    else:
        break

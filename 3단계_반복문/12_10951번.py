# 백준 10951번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램
# 특이사항: 테스트 케이스 개수가 주어지지 않으며, 0 0으로 끝나지도 않음(EOF 이용)
import sys
while True:
    try:
        x, y = map(int, sys.stdin.readline().split())
        print(x+y)
    except:
        break

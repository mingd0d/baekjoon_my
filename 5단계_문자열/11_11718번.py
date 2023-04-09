# 백준 11718번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 입력 받은 대로 출력하는 프로그램
import sys
while True:
    try:
        word = sys.stdin.readline().rstrip()
        if word != "":
            print(word)
        else:
            break
    except:
        break

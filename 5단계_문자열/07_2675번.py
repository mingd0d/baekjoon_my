# 백준 2675번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 문자열 S를 입력받은 후, 각 문자를 R번 반복한 새 문자열 P를 출력하는 프로그램
import sys
n = int(input())
newword = ""
d = [sys.stdin.readline().split() for k in range(n)]
for k in range(n):
    length = len(d[k][1]) # 단어 길이
    for p in range(length):
        newword = newword + d[k][1][p]*int(d[k][0])
    print(newword)
    newword = ""

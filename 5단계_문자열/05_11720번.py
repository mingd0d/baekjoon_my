# 백준 11720번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 공백 없이 쓰여진 N개의 숫자를 모두 합해서 출력하는 프로그램
n = int(input())
k = input()
s = 0
for i in range(n):
    s = s + int(k[i])
print(s)

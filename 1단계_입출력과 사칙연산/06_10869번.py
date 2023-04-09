# 백준 10869번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 두 자연수 A와 B가 공백으로 구분되어 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램
x, y = input().split()
x = int(x)
y = int(y)
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x%y)

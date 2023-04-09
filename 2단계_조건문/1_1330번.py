# 백준 1330번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 두 정수 A와 B가 공백으로 구분되어 주어졌을 때, A와 B를 비교하는 프로그램
x, y = input().split()
x = int(x)
y = int(y)
    
if x > y:
    print(">")
elif x == y:
    print("==")
else:
    print("<")

# 백준 10430번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 세 수 A, B, C가 공백으로 구분되어 주어졌을 때, 첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력하는 프로그램
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)
print((x+y)%z)
print(((x%z)+(y%z))%z)
print((x*y)%z)
print(((x%z)*(y%z))%z)

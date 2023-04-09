# 백준 2480번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 입력될 때, 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램(규칙은 문제 참고)
x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if x == y and y == z:
    print(10000+1000*x)
elif x == y:
    print(1000+(x*100))
elif y == z:
    print(1000+(y*100))
elif z == x:
    print(1000+(z*100))
else:
    if x > y and x > z:
        print(x*100)
    elif y > z and y > z:
        print(y*100)
    else:
        print(z*100)

# 백준 2525번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램
# 입력: 첫째 줄은 현재 시각의 시와 분을 공백으로 구분하여 입력, 둘째 줄은 조리 시간이 분 단위로 주어짐
x, y = input().split()
z = int(input())
x = int(x)
y = int(y)
a = (y+z)//60

if y+z < 60:
    print(x, y+z)
else:
    if x+a < 24:
        print(x+a, y+z-(a*60))
    else:
        print(x+a-24, y+z-(a*60))

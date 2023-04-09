# 백준 5622번 풀이
# 작성자: 숙명여자대학교 2311332 강민지
# 설명: 다이얼을 걸기 위해서 필요한 최소 시간을 출력하는 프로그램
word = input()
length = len(word)

d = []
for k in range(length):
    d.append(ord(word[k]))

time = 0
for k in range(length):
    time = time + 2
    if d[k] <= 79: # O까지
        if (int(d[k])-64)%3 != 0:
            time = time + 1 + (int(d[k])-64)//3
        else:
            time = time + (int(d[k])-64)//3
    else:
        if d[k] <= 83: # s까지
            time = time + 6
        else:
            if d[k] <= 86: # v까지
                time = time + 7
            else: # 나머지
                time = time + 8
print(time)

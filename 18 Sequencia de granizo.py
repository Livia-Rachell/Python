#1441
def hight(num):
    return num != 0 and ((num & (num - 1)) == 0)

while True:
    h = int(input())
    if h == 0:
        break
    m = 0
    while hight(h) != True:
        if h > m:
            m = h
        if h % 2 == 0:
            h = int(h/2)
        else:
            h = h*3 + 1
    if h > m:
        m = h
    print(m)
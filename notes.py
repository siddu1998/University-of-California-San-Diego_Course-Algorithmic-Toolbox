import sys

t = int(input())

while t > 0:
    count = 0
    rs = int(input())

    if rs >= 100:
        count += (rs // 100)
        rs = rs - (100 * (rs // 100))
    if rs >= 50:
        count += (rs // 50)
        rs = rs - (50 * (rs // 50))
    if rs >= 10:
        count += (rs // 10)
        rs = rs - (10 * (rs // 10))
    if rs >= 5:
        count += (rs // 5)
        rs = rs - (5 * (rs // 5))
    if rs >= 2:
        count += (rs // 2)
        rs = rs - (2 * (rs // 2))

    if rs >= 1:
        count += (rs // 1)
        rs = rs - (rs // 1)

    print(count)
    t -= 1



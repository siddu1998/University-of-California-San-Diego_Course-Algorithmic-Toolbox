from math import gcd

T = int(input())
for recipes in range(T):
    recipe = list(map(int, input().split()))
    N = recipe[0]
    recipe = recipe[1:]
    netGCD = recipe[0]
    for i in range(1, N):
        netGCD = gcd(recipe[i], netGCD)
    for i in recipe:
        print(i // netGCD, end=' ')
    print()
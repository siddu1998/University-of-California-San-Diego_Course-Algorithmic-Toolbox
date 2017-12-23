def sum_digit(n):
    s = 0
    while n:
        n, remainder = divmod(n, 10)
        s += remainder
    return (s)


test_list=[int(input()) for i in range(int(input()))]
ans=[]
for i in range(len(test_list)):
    ans.append(sum_digit(test_list[i]))





print(*ans,sep='\n')

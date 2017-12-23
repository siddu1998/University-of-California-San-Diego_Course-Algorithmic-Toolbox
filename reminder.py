test_cases=int(input())
input_list=[]
answer_list=[]
for i in range(test_cases):
    A,B = input().split(' ')
    A=int(A)
    B=int(B)
    answer_list.append(A%B)

print(*answer_list,sep='\n')


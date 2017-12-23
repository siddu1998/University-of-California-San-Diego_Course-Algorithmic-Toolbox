import math
question_list=[]

for i in range (int(input())):
    question_list_element=int(input())
    question_list.append(math.factorial(question_list_element))


print(*question_list,sep='\n')



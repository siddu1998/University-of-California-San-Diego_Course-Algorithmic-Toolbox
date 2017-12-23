def get_sign(number_list_element):
    if number_list_element[0]<=1000:
        return number_list_element[0]*number_list_element[1]
    else:
        return (number_list_element[0]*(number_list_element[1]-(number_list_element[1]*0.1)))

number_list=[]
symbol_list=[]

for i in range(int(input())):
     A,B=map(float,input().split())
     number_list.append((A,B))
     symbol_list.append(get_sign(number_list[i]))

print(*symbol_list,sep='\n')
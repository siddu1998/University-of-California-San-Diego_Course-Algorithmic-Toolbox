def check_rainbow(a):
    if len(a)%2!=0:
        first_half=a[:int(len(a)/2)]
        second_half=a[int(len(a)/2):][::-1]
        if first_half==second_half:
            if max(set(a))-min(set(a))+1==len(set(a)):
                        return ('yes')
            else:
                        return ('no')
        else:
            return ('no')
    if len(a)%2==0:
        first_half_odd=a[:int(len(a)/2)+1]
        second_half_odd=a[int(len(a)/2):][::-1]
        if first_half_odd==second_half_odd:
            if max(set(a))-min(set(a))+1==len(set(a)):
                        return ('yes')
            else:
                        return ('no')
        else:
            return ('no')

test_cases=int(input())
rainbow_list = []
yes_no_list=[]
for i in range(test_cases):
    for j in range(int(input())):
        rainbow_list.append(int(input()))

    yes_no_list.append(check_rainbow(rainbow_list))

print(*yes_no_list)
def partition(a,start,end):
    pivot=a[end]
    pIndex=start
    for i in range(start,end):
        if a[i]<=pivot:
            a[i],a[pIndex]=a[pIndex],a[i]
            pIndex=pIndex+1

    a[end],a[pIndex]=a[pIndex],a[end]
    return pIndex

def quicksort(a,start,end):
    if start<end:
        pi = partition(a,start,end)
        quicksort(a,start,pi-1)
        quicksort(a,pi+1,end)




a=[7, 10, 4, 3, 20, 15]
n=int(input("please enter the nth largest element you want to find"))
quicksort(a,0,len(a)-1)
print(a[n-1])
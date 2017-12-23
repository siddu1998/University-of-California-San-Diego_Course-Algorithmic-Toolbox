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
        pi=partition(a,start,end)
        quicksort(a,start,pi-1)
        quicksort(a,pi+1,end)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Sorted array is:")
print(*arr,sep=" "),

def merge_two_sorted_lists(arr,a,b):
    len_a=len(a)
    len_b=len(b)
    i=j=k=0
    while i<len_a and j<len_b:
        if(a[i]<=b[j]):
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1
    while i<len_a:
        arr[k]=a[i]
        i+=1
        k+=1
    while j<len_b:
        arr[k]=b[j]
        j+=1
        k+=1

def merge_sort(arr):
    if len(arr)<=1:
        return 
    mid=len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    merge_two_sorted_lists(arr,left_arr,right_arr)
l=[90,76,2,67,3,90]
merge_sort(l)
print(l)
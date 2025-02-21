def bubble_sort(arr):
    size=len(arr)
    for i in range(size-1):
        swapped=False
        for j in range(size-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
        if swapped==False:
            break
elements=[1,2,4]
bubble_sort(elements)
print(elements)


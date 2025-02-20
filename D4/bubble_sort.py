def bubble_sort(arr):
    for i in range(len(arr)-1):
        sorted=True
        for j in range(len(arr)-i-1):
            if(arr[j]>arr[j+1]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
                sorted=False
        if sorted:
            return arr
        
arr=[2,1,4,9]
print(bubble_sort(arr))
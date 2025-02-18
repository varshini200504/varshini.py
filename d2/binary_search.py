def binarysearch(array,search_element):
    hig=len(array)
    low=0
    while low<=high:
        mid=(low+high)//2
        if(array[mid]==search_element):
            return mid
        elif search_element<array[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
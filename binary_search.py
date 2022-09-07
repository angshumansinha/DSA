from insertion_sort import ins_sort
from math import *

class binary_search:
    def __init__(self):
        pass

    def bin_search(array,value):
        #array needs to be sorted
        flag=0
        sorted_arr=ins_sort.sort(array)
        #print(sorted_arr)
        low=0
        high=len(sorted_arr)-1
        while low<=high:
            mid=floor((low+high)/2)
            if sorted_arr[mid]==value:
                flag=1
                break
            elif value>sorted_arr[mid]:
                low=mid+1
            else:
                high=mid-1
        if flag==0:
            return "not found"
        else:
            return "value found at ",mid



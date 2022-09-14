#binary search using recursion
import math as mt
def isSorted(array,size):
    i=0
     #requirement of array in binary search is that it needs to be sorted
     #base case
    if size==0 or size==1:
        #one element means array is already sorted or no element means nothing to sort
        return True
    if array[0]>array[1]:# not sorted
        return False #solving just one case
    else:
        i+=1
        return isSorted(array[i:],size-1) #recursive case


def BinarySearch(array,start,end,size,key):
    #base condition
    if not isSorted(array,size) or start>end:
        return False
    #lets calculate mid
    mid=mt.floor((start + end) /2)
    if array[mid]==key:
        return True
    if array[mid]>key:
        end=mid-1
        return BinarySearch(array,start,end,size,key)
    else:
        start=mid+1
        return BinarySearch(array,start,end,size,key)


arr=[11,1,3,4,5,13]
start=0
size=len(arr)
end=size-1
res=BinarySearch(arr,start,end,size,3)
if res:
    print("Value Found")
else:
    print("Not Found or Array needs to be sorted")
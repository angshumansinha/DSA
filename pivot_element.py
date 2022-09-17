#find the pivot of an array using binary search 

#[10,12,13,1,3,4]
"""
Let's visualise the above array
^
|
|                13
|            12
|        10                      4  (e)
|      (s)                   3
|                       [1]--------------> Pivot element
|                      
----------------------------------------------------------->

let l1={10,12,13} #this can be line l1 l1--->relation : arr[mid]>arr[0]
l2={1,3,4} this can be line l2------> arr[mid]>arr[mid+1]

#Binary search mein saraa khel mid ka hai

Pseudocode

mid=s+(e-s)/2
while(s<e):
    if arr[mid]>arr[0]:
        s=mid+1
    else: 
        e=mid
    mid=s+(e-s)/2
return mid

"""
import math as mt
def pivot_element(array):
    s=0
    e=len(array)-1
    mid=mt.floor((s+e)/2)
    while(s<e):
        if array[mid]>array[0]:
            s=mid+1
        else:
            e=mid
        mid=mt.floor((s+e)/2)
    return s


arr=[13,14,15,-1,2,3,4]
print(arr[pivot_element(arr)])





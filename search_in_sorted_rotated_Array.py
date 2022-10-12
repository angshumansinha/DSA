#search in a sorted and rotated array
"""


arr=[1,2,3,4,5,6,7,8,9] ------------->sorted array

rotated_arr=[7,8,9,1,2,3,4,5,6] ----------> sorted plus rotated array
                        9
                        8
                        7
                        (s)     6 (e)                
                                5
                                4
                                3
                                2
                                1

#find pivot of the array
 if in second line : arr[pivot]<target<arr[n-1]
 if in first line: arr[0]<target<arr[pivot-1]
"""

import math as mt
def pivot_index(array):
    s=0
    e=len(array)-1
    mid=mt.floor((s+e)/2)
    while (s<e):
        if array[mid]>=array[0]:
            s=mid+1
        else:
            e=mid
        mid=mt.floor((s+e)/2)
    return s

def rotated_binary_search(array,key):
    s=0
    flag=0
    e=len(array)-1
    mid=mt.floor((s+e)/2)
    while s<=e:
        if array[mid]==key:
          flag=1
          break
        elif array[mid]<key:
            s=mid+1
        else:
            e=mid-1
        mid=mt.floor((s+e)/2)
    if flag==0:
        return False
    else:
        return mid  




arr=[7,8,9,1,2,3,4,5,6]
key=3
pi=pivot_index(arr)
if arr[pi]<=key<=arr[len(arr)-1]:
    print(pi+(rotated_binary_search(arr[pi:len(arr)],key)))
else:
    print(rotated_binary_search(arr[pi:len(arr)],key))
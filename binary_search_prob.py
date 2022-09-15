#binary search problems
#first and last position of an element of an array in a sorted element
#leftmost occurence and rightmost occurence
#binary search time complexity O(logn)
import math as mt
def first_occurence(array,key):
    start=0
    end=len(array)-1
    mid=mt.floor((start+end)/2)
    while (start <= end):
        #three conditions
        if array[mid]==key:
            #store the answer
            ans=mid
            #checking first_occurence
            end=mid-1
        elif array[mid]<key:
            start=mid+1
        elif array[mid]>key:
            end=mid-1
        mid=mt.floor((start+end)/2)
    return ans

def last_occurence(array,key):
    start=0
    end=len(array)-1
    mid=mt.floor((start+end)/2)
    while (start <= end):
        #three conditions
        if array[mid]==key:
            #store the answer
            ans=mid
            #checking last_occurence
            start=mid+1
        elif array[mid]<key:
            start=mid+1
        elif array[mid]>key:
            end=mid-1
        mid=mt.floor((start+end)/2)
    return ans

arr=[11,12,13,14,14,14]
print(last_occurence(arr,14))
        
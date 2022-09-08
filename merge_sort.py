#Fastest sorting algorithm
#Time complexity O(nlogn)
#MergeSort L ---> MergeSort Right -----> Merge
#Uses Recursion

import math
#General Idea that one element in a list is always sorted

#approaches
#copy values into two list and sort them
#use indexes

def Merge(arr,lb,mid,ub):
    len1=mid-lb +1
    len2=ub-mid
    #create a ref that points to the position in the main list
    mainArrayindex=lb

    first_array=len1*[None]
    second_array=len2*[None]
    #copy values
    #first array
    for i in range(0,len1):
        first_array[i]=arr[mainArrayindex]
        mainArrayindex+=1
    
    #second array
    for i in range(0,len2):
        second_array[i]=arr[mainArrayindex]
        mainArrayindex+=1

    
    #merge the array
    index1=0
    index2=0
    mainArrayindex=lb

    #both have equal lengths
    while (index1<len1 and index2<len2):
        if first_array[index1]<second_array[index2]:
            arr[mainArrayindex]=first_array[index1]
            index1+=1
        else:
            arr[mainArrayindex]=second_array[index2]
            index2+=1
        mainArrayindex+=1

    #if one has a greater length and doesnt satisy above condition
    while (index1<len1):
        arr[mainArrayindex]=first_array[index1]
        index1+=1
        mainArrayindex+=1
    
    while (index2<len2):
        arr[mainArrayindex]=second_array[index2]
        index2+=1
        mainArrayindex+=1
    
    print(arr)



def MergeSort(arr,lb,ub):
    if lb>=ub: #no element or one element
        return
    mid=math.floor((lb+ub)/2)
    MergeSort(arr,lb,mid)
    MergeSort(arr,mid+1,ub)
    Merge(arr,lb,mid,ub)


arr=[1,3,2,2,-5,9,0]
MergeSort(arr,0,len(arr)-1)
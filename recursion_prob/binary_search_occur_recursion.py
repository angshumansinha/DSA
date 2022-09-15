#binary search problems
#first and last position of an element of an array in a sorted element
#leftmost occurence and rightmost occurence
#binary search time complexity O(logn)
#ans is passed as a parameter because in recursion every time a function call is made , it wont remember the 
#values if not passed to the next call
import math as mt
def first_occurence(array,start,end,key,ans):
    print(array, start, end)
    if start>end:
        return ans #base case
    mid=mt.floor((start+end)/2)
    if array[mid]==key:
        ans=mid
        end=mid-1
        return first_occurence(array,start,end,key,ans)
    #recursive case
    elif array[mid]>key:
        end=mid-1
        return first_occurence(array,start,end,key,ans)
    else:
        start=mid+1
        return first_occurence(array,start,end,key,ans)

def last_occurence(array,start,end,key,ans):
    if start>end:
        return ans 
    mid=mt.floor((start+end)/2)
    if array[mid]==key:
        ans=mid
        start=mid+1
        return last_occurence(array,start,end,key,ans)
    #recursive case
    elif array[mid]>key:
        end=mid-1
        return last_occurence(array,start,end,key,ans)
    else:
        start=mid+1
        return last_occurence(array,start,end,key,ans)
    

arr=[2,4,4,5,6]
start=first_occurence(arr,0,len(arr)-1,4,-1)
end=last_occurence(arr,0,len(arr)-1,4,-1)
print("number of occurences is ",(end-start)+1)




    
    
        


"""def last_occurence(array,key):
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
"""        
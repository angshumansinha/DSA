#linear search using recursion
def linearSearch(array,size,key):
    #print(array," ",size) to debug
    i=0 #to mark index of array
    #base case 
    if size==0: #if there is no element in the array or the search has exhausted for the entire list
        return False
    if array[0]==key: #at each recursion we check for the first element and compare if value is matched
        return True
    else:
        #recursive case
        i+=1 #increase the index and reduce the size by 1
        remPart=linearSearch(array[i:],size-1,key)
        return remPart

arr=[2,3,4,5,6]
size=len(arr)
ans=linearSearch(arr,size,11)
if ans:
    print("Value Found")
else:
    print("Not Found")
    
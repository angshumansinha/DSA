#sum of elements using recursion
def sum_array(array):
    i=0
    #base case
    if len(arr)==0 or len(arr)==1:
        return False
    else:
        i+=1 
        sum=array[0]+(sum_array(array[i]))
        return sum


arr=[1,2,3,4]
print(sum_array(arr))
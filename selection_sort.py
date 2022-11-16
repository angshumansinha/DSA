#basic steps to solve selection sort
#at each step find the minimum value and compare with the rest to check the least with the rest
#swap whats in the beginning
#increment the minimum
# no of passes is equal to the no of elements

def selection_sort(array):
    size=len(array)
    for i in range(size):
        minimum = i 
        for j in range(i+1,size):
            if array[minimum]>array[j]: #comparing with the rest of the element
                minimum=j
        #swap the elements
        array[i],array[minimum]=array[minimum],array[i]
    return array

array=[15,14,-1,0,6,8,5]
print(selection_sort(array))

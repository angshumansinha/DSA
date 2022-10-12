# binary search
import math as mt
def BinarySearch(number):
    ans=-1
    s=0
    e=number
    mid=mt.floor((s+e)/2)

    while s<=e:
        if mid**2==number:
            return mid
        elif mid**2<number:
            s=mid+1
            ans=mid
        else:
            e=mid-1
        mid=mt.floor((s+e)/2)


    return ans

def morePrecision(ans,precision,number):
    factor=1
    i=0
    while i<precision:
        factor=factor/10
        j=ans
        while j**2<=number:
            ans=j
            j+=factor
        i+=1
    
    return ans

ans=BinarySearch(6.25)
print(morePrecision(ans,3,6.25))

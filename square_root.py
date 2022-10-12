#square root using binary search
import math as mt
def square_root(value):
    l1=[int(x) for x in range(0,value+1)]
    s=0
    e=len(l1)-1
    mid=mt.floor((s+e)/2)
    ans=-1
    while s<=e:
        square=int(l1[mid]**2)
        if square>value:
            e=mid-1
        elif square<value:
            s=mid+1
            ans=l1[mid]
        else:
            return l1[mid]
        mid=mt.floor((s+e)/2)
    return ans

print(square_root(123456))
        

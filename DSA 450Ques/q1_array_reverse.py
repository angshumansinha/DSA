#reverse an array
arr=[2,3,4,5,6]
#reverse it
#one way to do it is keep pointers and keep shufling
head=0
tail=len(arr)-1
while head<tail:
    #swap
    temp=arr[head]
    arr[head]=arr[tail]
    arr[tail]=temp
    head+=1
    tail-=1
print(arr)

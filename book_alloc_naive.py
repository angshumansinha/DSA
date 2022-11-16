import math as mt

def isPossibleSoln(books,n,m,mid):
    temp = 0
    i=0
    pageSum=0
    while i<m:
        pageSum=0
        while pageSum<=mid and temp<n:
            pageSum+=books[temp]
            temp+=1
        i+=1
    if temp==n:
        return True
    else:
        return False




def BookAllocaton(books,m):
    ans=-1
    n=len(books)
    s=0
    e=sum(books)
    mid=mt.floor((s+e)/2)
    while s<=e:
        if isPossibleSoln(books,n,m,mid):
            e=mid-1
            ans=mid
        else:
            s=mid+1
        mid=mt.floor((s+e)/2)

    return ans

books=[10,20,30,40]
m=2
print(BookAllocaton(books,m))
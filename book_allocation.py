import math as mt

def isPossibleSoln(books,n,m,mid):
    studentCount=1
    pageCount=0
    i=0
    while i<n:
        if pageCount+books[i]<=mid:
            pageCount+=books[i]
        else:
            studentCount+=1
            if studentCount> m or books[i]>mid:
                return False
            pageCount=books[i]
        i+=1
    return True




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
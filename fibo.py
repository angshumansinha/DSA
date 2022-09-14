#without recursion
def fibo(n):
    n1=0
    n2=1
    sum=0
    i=3
    print(n1)
    print(n2)
    while(i<=n):
        sum=n1+n2
        print(sum)
        n1=n2
        n2=sum
        i+=1

fibo(10)

#with recursion we print the nth term of fibonacci
def rec_fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    sum=rec_fibo(n-1)+rec_fibo(n-2)
    return sum

print(rec_fibo(6))


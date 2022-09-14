#let's understand recursion
#developing a recurrence relation
# finding base case and recursive case

#ex 1
def power(n):
    #to stop the recursion we need to stop
    #base case ---> return statement is mandatory
    if n==0:
        return 1
    
    #recusive relation f(n)=n*f(n-1)
    return 2*power(n-1)


print(power(2))

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

#tail recursion
#def print_count(n):
    if n==0:
        return
    print(n)
    return print_count(n-1)

#print_count(8)
print(factorial(7))

#head recursion
def print_count(n):
    if n==0:
        return
    return print_count(n-1)
    print(n)

print_count(8)


#without base it will not stop and the function call stack will have an overflow condition

def fibonacci(n):
    n1=0
    n2=1

    while n2<=n:
        sum=n1+n2
        n1=sum
        n2+=1
        print(n1," ",n2)

print(fibonacci(5))

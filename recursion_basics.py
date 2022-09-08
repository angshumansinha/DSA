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

print(factorial(7))

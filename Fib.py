def fib(n):

    #this is the base case.. this is actually important
    if n <= 3:
        return n 
    
    return fib(n-1) + fib(n-2)

print(fib(6))

# this is like stack overflow
# recursion is useful



# Defining Functions
def fibonacci(k):    # This is a Fibonacci series up to k
    """Print a Fibonacci series up to k."""
    x, y = 0, 1
    while y< k:
        print (y)
        x, y = y, x+y
 
#calling the function
fibonacci(2000) #in this case I've set k=2000
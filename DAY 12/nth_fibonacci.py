#nth fibonacci series
def nth_fibo(n):
    if n==1 or n==2:
        return n-1
    
    return nth_fibo(n-1)+nth_fibo(n-2)
print(nth_fibo(10))

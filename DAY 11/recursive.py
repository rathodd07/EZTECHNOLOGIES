'''def fun(n):
    if n<=2:
        return
    fun(n-2)
    fun(n-4)
    print(n)
fun(8)'''
import time
def fun(n):
    if n<=2:
        return n
    return fun(n-4)+fun(n-2)
start_time=time.time()
print(fun(16)) 
end_time=time.time()
execution_time=end_time-start_time
print(execution_time)
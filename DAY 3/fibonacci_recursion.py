#1.method 1
'''def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(10)

What is Fibonacci Series in Python?
The Fibonacci series is a sequence of numbers in which each 
number is the sum of the two preceding ones.
In Python, the Fibonacci series can be implemented using a loop or recursion.
It starts with 0 and 1, and each subsequent number is the sum of the two previous numbers. 
For example, the Fibonacci series begins as 0, 1, 1, 2, 3, 5, 8, 13, and so on.

Mathematically, we can denote it as:
Fn = Fn-1 + Fn-2

Where, Fn denotes the nth term of Fibonacci series.
The first two terms of this series are considered to be:
F0 = 0 (Zeroth term of Fibonacci sequence)
F1 = 1 (First term of Fibonacci sequence)

Now, by using the above two values we can easily calculate all other terms of Fibonacci
series as follows:
F2 = F1 + F0 = 0 + 1 = 1
F3 = F2 + F1 = 1 + 1 = 2
F4 = F3 + F2 = 2 + 1 = 3
Series is 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ……
Problem Solution
In fibonacci series the first two numbers in the Fibonacci sequence 
are 0 and 1 and each subsequent number is the sum of the previous two.
'''
#2.using recursion:
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))

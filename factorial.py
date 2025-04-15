import sys
sys.setrecursionlimit(10**6)
def factorial(n):
    if n < 0 :
        return "not defined"
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
f=int(input("enter the number:"))
print("factorial of a given no:",factorial(f))
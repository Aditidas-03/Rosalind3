
#here the solution is 2n-5 but with modulo to take care of overflow
def double_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * double_factorial(n - 2)
    
m=1000000
n=971#input n less than 1000 here

result=double_factorial(2 * n - 5) % m
print(result)

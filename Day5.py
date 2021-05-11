#Mohamed Diallo - Day 5: 05/08/2021
#Description: Given n, calculate the factorial.

def factorial(n):
    fact, i = 0, n -1
    if(n==0 or n==1):
        return 1
    else:
        fact = n
        while(i != 1):
            fact *= i
            i -= 1
        return fact

print(factorial(1))
'''def factorial(n):
  if n == 0:
    return 1

  return n * factorial(n-1)
'''

def factorial(n):
    factorial = None
    if n == 0:
        return 1
    elif n > 0 :
        factorial = 1
        for number in range(1,n+1):
            factorial *= number

    return factorial


print(factorial(3))

def f(n):
    if n == 0:
        return 1
    return n - m(f(n - 1))

def m(n):
    if n == 0:
        return 0
    return n - f(m(n - 1))



print(f(0))
print(f(5))
print(f(10))

print(m(0))
print(m(5))
print(m(10))

#Casos Test
#f(0) ==> 1
#f(5) ==> 3
#f(10) ==> 6
#m(0) ==> 0
#m(5) ==> 3
#m(10) ==> 6

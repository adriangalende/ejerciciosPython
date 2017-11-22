
#recursivo
'''def fibonacci(numero):
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero-1) + fibonacci(numero-2)
'''
def fibonacci(numero):
    proximo = 0
    actual = 1
    i = 0
    while i <= numero:
        actual,proximo = proximo, actual+proximo
        i+=1
    return actual


print(fibonacci(36))

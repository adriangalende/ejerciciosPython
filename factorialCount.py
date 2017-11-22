import math

def contarDigitosFactorial(n):
    #Kamenetsky's formula ==> (log⁡(2πn)/2+n(log⁡n−log⁡e))/log⁡10]+1
    x = (math.log(2*math.pi*n)/2+n*(math.log(n)-math.log(math.e)))/math.log(10) +1

    return int(x)

print(contarDigitosFactorial(5000000000))

#Test
#contarDigitosFactorial(0)
#>>1
#contarDigitosFactorial(5)
#>>3
#contarDigitosFactorial(50)
#>>65
#contarDigitosFactorial(500)
#>>1135

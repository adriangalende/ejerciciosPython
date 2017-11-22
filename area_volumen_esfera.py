# Calcular area y volumen de una esfera
import math
def areaEsfera(radio):
  return 4 * math.pi * int(radio)**2

def volumenEsfera(radio):
  return 4 * math.pi * int(radio) ** 3 / 3.0




radioEnMetros = input("Introduce el radio (en metros) para calcular el área y volumen de la esfera")

print( "Area = " + str(areaEsfera(radioEnMetros)) + "m2")
print( "Volumen = " + str(volumenEsfera(radioEnMetros))+ "m3")



#casos Test

#radioEnMetros = 1
#>> A= 4.18879, V=12.57

# radioEnMetros = 3
#>> A = 113.09734, V = 113.10

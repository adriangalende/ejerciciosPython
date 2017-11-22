def rgb(r, g, b):
  listaRGB = [r,g,b]
  result = ""
  for element in listaRGB:
    element = 0 if element < 0 else 255 if element > 255 else element
    result += '0' + hex(element).split('x')[1].upper() if int(element) < 10 else hex(element).split('x')[1].upper()
  return result



print(rgb(10,2,3))
#test.assert_equals(rgb(0,0,0),"000000", "testing zero values")
#test.assert_equals(rgb(1,2,3),"010203", "testing near zero values")
#test.assert_equals(rgb(255,255,255), "FFFFFF", "testing max values")
#test.assert_equals(rgb(254,253,252), "FEFDFC", "testing near max values")
#test.assert_equals(rgb(-20,275,125), "00FF7D", "testing out of range values")

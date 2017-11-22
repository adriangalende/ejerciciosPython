#solucion con expresion regular

'''import re
def is_valid_IP(ip):
  regex = re.match('^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$',ip)

  return False if regex == None else True'''


def ipValidator(ip):
  listaOctetos = ip.split('.')
  if len(listaOctetos) < 4:
    return False

  for octeto in listaOctetos:
    try:
      int(octeto)
    except ValueError:
      return False
    else:

      if not(int(octeto) >= 0 and int(octeto) <= 255) or ( len(octeto) > 1 and octeto[0] == "0") or (len(octeto.split(" ")) > 1) :
        return False

  return True

print(ipValidator('12.244.56.1'))

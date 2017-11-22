def camelCase(string):
  camelString = ""
  for word in string.split(" "):
    camelString += word[0].upper() + word[1:]
  return camelString

print(camelCase("camel case word"))
#camelcase("hello case") => HelloCase
#camelcase("camel case word") => CamelCaseWord

import re


def converte(n, base):
  if n < base:
    return str(n)
  else:
    return converte(n//base, base) + str(n%base) 

# Coloque aqui sua expressão regular
regexp = r'c*a[ac]*b[abc]*|c*b[b,c]*a[abc]*'


s = ""
translation = s.maketrans("120","abc")
        
for i in range(1,40):
  string = converte(i, 3)  
  print(">>>>>>>>")
  string = string.translate(translation)  
  print(string) 
  print("========")
  print( re.fullmatch(regexp,string) != None  )  
  print("<<<<<<<<")





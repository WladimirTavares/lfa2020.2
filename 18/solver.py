import re



# Coloque aqui sua expressão regular
regexp = r'(0|10)*11(0|01)*|(0|10)*(0|01)*|(0|10)*1(0|01)*'

#regexp = r'[01]*(00|11)[01]*'


        
for i in range(1,40):
  string = "{0:b}".format(i)    
  print(">>>>>>>>")
  print(string) 
  print("========")
  print( re.fullmatch(regexp,string)  != None )  
  print("<<<<<<<<")





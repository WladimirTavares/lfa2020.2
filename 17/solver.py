import re



# Coloque aqui sua expressão regular
regexp = r'[0-1]*1[0-1]{3}'


        
for i in range(1,40):
  string = "{0:b}".format(i)    
  print(">>>>>>>>")
  print(string) 
  print("========")
  print( re.match(regexp,string) )  
  print("<<<<<<<<")





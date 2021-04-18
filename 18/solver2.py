import re

# Coloque aqui sua expressão regular
regexp = r'(0|10)*11(0|01)*|(0|10)*(0|01)*|(0|10)*1(0|01)*'

print( re.fullmatch(regexp,string) != None  )  

        





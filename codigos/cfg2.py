# encoding: iso-8859-1
# Todo nao terminal será representado por uma letra maiúscula
# Todo terminal será representado por uma letra minúsculas
# O conjunto de regras é representado por uma lista de pares ordenado

 
  
grammar1 = [ 
      ("S", "aS" ), #rule 0           
      ("S", ""   ), #rule 1               
]

initial = "S"


#Um derivação será representada por uma lista de índices das regras


def check_derivation(grammar, sentencial_form, derivation, string):
  print sentencial_form
  
  for i in range(len(derivation)):
    rule_index = derivation[i]    
    found = False    
    for pos in range( len(sentencial_form) ):      
      symbol = sentencial_form[pos]
      if symbol == grammar[rule_index][0]:
        sentencial_form = sentencial_form[0:pos] + grammar[rule_index][1] + sentencial_form[pos+1:]
        found = True
        break
    
    if not found:
      print "derivacao mal formada"
      return 

    print "=>" + sentencial_form        
  
  if sentencial_form == string:
    print "derivacao completa"
  else:
    print "derivacao imcompleta" 


#check_derivation(grammar1, "S", [0,1,0,1,1], "aaa") 


#check_derivation(grammar1, "S", [0,1], "a") 
#S
#=>aS
#=>a
#derivacao completa


#check_derivation(grammar1, "S", [0,0,0,1], "aaaa")
#S
#=>aS
#=>aaS
#=>aaaS
#=>aaa
#derivacao imcompleta 


#check_derivation(grammar1, "S", [0,0,0,1], "aaa")  
#S
#=>aS
#=>aaS
#=>aaaS
#=>aaa
#derivacao completa



#check_derivation(grammar1, "S", [1,0,0,0], "aaa") 
#S
#=>
#derivacao mal formada


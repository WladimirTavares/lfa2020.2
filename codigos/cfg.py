grammar1 = [ 
      ("S", [ "a", "S" ] ), #rule 0           
      ("S", [ "" ])       , #rule 1               
]

grammar2 = [ 
      ("S", [ "S", "a" ] ), #rule 0           
      ("S", [ "" ])       , #rule 1               
]

grammar3 = [ 
      ("S", [ "S", "S" ] ), #rule 0           
      ("S", [ "a" ])       , #rule 1               
]

grammar4 = [ 
      ("S", [ "a", "a", "S" ] ), #rule 0           
      ("S", [ "" ])       , #rule 1               
]


def non_terminal(grammar, symbol):
  for rule in grammar:
    if symbol == rule[0]:
      return True    

def terminal(grammar, symbol):
  return not non_terminal(grammar, symbol)

def is_null(grammar, visited, symbol):
  #print ("symbol: " + symbol )  
  #print ("visited: " + str(visited) )
  
  if symbol == "":
    return True  
      
  if symbol in visited:
    return False

  if terminal(grammar, symbol):
    return False  
 
  visited = visited + [symbol]  
  for rule in grammar:
    #print rule
    if rule[0] == symbol:
      if all( is_null(grammar, visited, rhs) for rhs in rule[1] if rhs != "" ):
        return True
  return False           

#print is_null(grammar1, [], "S")
#print is_null(grammar2, [], "S")


def expand(tokens_and_derivation, grammar):
  (tokens, derivation) = tokens_and_derivation
  for token_pos in range(len(tokens)): # for each rule
    for rule_index in range(len(grammar)): # for each rule
      rule = grammar[rule_index]
      if tokens[token_pos] == rule[0]: #token is on left hand side of rule
        lhs = tokens[0:token_pos] + rule[1] + tokens[token_pos+1:]
        yield ( lhs , derivation + [rule_index])

def size_tokens(grammar, tokens):
  cont = 0  
  for symbol in tokens:
    if symbol != "" and not is_null(grammar, [], symbol):
      cont = cont + 1
  return cont

def accept(grammar, start, utterance): 
  enumerated = [ ([start], [] )] 
  
  while True:
    new_enumerated = enumerated
    
    print "new_enumerated:" + str(new_enumerated)

    for u in enumerated:
      for i in expand(u, grammar):
        if not i in new_enumerated:
          (tokens, derivation) = i
          #print "tokens: " + str(tokens)
          #print "size tokens: " + str(size_tokens(grammar, tokens) )
          if size_tokens(grammar, tokens) <= len(utterance):          
            new_enumerated = new_enumerated + [i]
  
    if new_enumerated != enumerated:
      enumerated = new_enumerated
    else:
      break
  for x in enumerated:
    result =  "".join(x[0])
    #print result 
    if result == utterance:
      return x[1]
  return []

    
#print accept(grammar1, "S", "aaa")
#print accept(grammar2, "S", "aaa")
#print accept(grammar3, "S", "aaa")
#print accept(grammar4, "S", "aaaa")

def derivation(grammar, sentencial_form, derivation):
  #print derivation  
  print sentencial_form
  
  for i in range(len(derivation)):
    rule_index = derivation[i]    
    for pos in range( len(sentencial_form) ):      
      symbol = sentencial_form[pos]
      #print str(pos) + ":" + symbol      
      #print grammar[rule_index][0]
      #print grammar[rule_index][1]
      
      if symbol == grammar[rule_index][0]:
        #print "OK"
        sentencial_form = sentencial_form[0:pos] + "".join(grammar[rule_index][1]) + sentencial_form[pos+1:]
        #print sentencial_form
        break
    print "=>" + sentencial_form        
     
  

sequence = accept(grammar1, "S", "aaa")
derivation(grammar1, "S", sequence)
 
grammar5 = [ 
      ("E", [ "E", "+", "T" ] ), #rule 0           
      ("E", [ "T" ])       , #rule 1
      ("T", [ "T", "*", "F" ] ), #rule 2           
      ("T", [ "F" ])       , #rule 3               
      ("F", [ "(", "E", ")" ])       , #rule 4               
      ("F", [ "a" ])       , #rule 5               

]


sequence = accept(grammar5, "E", "a+a*a")
derivation(grammar5, "E", sequence)



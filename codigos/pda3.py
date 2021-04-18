# Pushdown automata 
# L = { w | n_a(w) = n_b(w) }
# L = { w | número de a's em w é igual ao número de b's em w }

# Context-Free Grammar
# S -> aSbS | bSaS | epsilon 

# Seja w uma string em L então podemos encontrar um prefixo de w com o mesmo número de #a's e b's então a string w pode ser reescrita como w = w1w2. 
# Considere dois casos:
# Caso 1: se w começa com a então 
# w1 começa com a e termina com b então w1 pode ser reescrito como w1 = axb
# x tem o mesmo número de a's e b's
# Regra: se x \in L e y \in L então axby \in L
# Caso 2: se começa com b então
# De maneira análoga:
# Regra: se x \in L e y \in L então bxay \in L


class PDA:
  def __init__(self, initial, edges, accepting):
    self.initial    = initial
    self.edges      = edges
    self.accepting  = accepting    
  
  def clousure(self, state, string, stack):
    print( "state => %d, string => %s, stack = %s" % (state, string, "".join(stack)))
    #print( "Stack: ")     
    #for x in stack:
    #  print( "%c " % (x) )
    
    top = stack[-1]
    stack = stack[0:-1]  
    
    if (state, '', top) in edges:
      #print( "(%d, '' , %c)" % (state, top) )        
      (next, topAux) = edges[(state, '', top)]
      #print( "next => %d " % next )        
      topAux.reverse()
      stackAux = stack.copy()
      stackAux.extend (topAux)
      if self.clousure(next, string, stackAux):
        return True
      else:
        print("backtrack")  

    if string == "":
      return state in accepting
    else:    
      char = string[0]
      remainder = string[1:]    
      #print( "(%d, %c , %c)" % (state, char, top) )  
      
      if (state, char, top) in edges:
          (next, topAux) = edges[(state, char, top)]         
          #print( "next => %d " % next )        
          topAux.reverse()                
          stackAux = stack.copy()
          stackAux.extend (topAux)        
          return self.clousure(next, remainder, stackAux)
      else:
        #print ("no edges")        
        return False
  
  def accept(self, string):
    stack = ['$']    
    return self.clousure(initial, string, stack)
        
  

    

initial = 0
edges = {
  
  #Empilhando w   
  (0, 'a', '$')  : (0, ['a','$']), 
  (0, 'b', '$')  : (0, ['b','$']),
  (0, 'a', 'a')  : (0, ['a','a']),
  (0, 'a', 'b')  : (0, []),
  (0, 'b', 'a')  : (0, []),
  (0, 'b', 'b')  : (0, ['b','b']),
  
  
  # Indo pro estado final
  (0, ''  , '$')  : (1, ['$'])

} 
accepting = [1]

string = "abba"

P = PDA(initial, edges, accepting)

print( P.accept(string) )



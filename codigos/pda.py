# Pushdown automara 
# L = { a^b^n | n >= 0}

# Context-Free Grammar
# S -> aSb | epsilon 


class PDA:
  def __init__(self, initial, edges, accepting):
    self.initial    = initial
    self.edges      = edges
    self.accepting  = accepting    
  
  def clousure(self, state, string, stack):
    print( "state => %d, string => %s, stack = %s" % (state, string, "".join(stack)))
    
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
  # empilha os a's iniciais
  (0, 'a', '$')  : (0, ['a','$']),
  (0, 'a', 'a')  : (0, ['a','a']),

  # Encontra um b após uma sequencia de a's  
  (0, 'b', 'a' ) : (1, []),
  
  # Caso a string seja vazia  
  (0, '' , '$' ) : (1, ['$']),
  
  # desempilha um b para cada a  
  (1, 'b' , 'a' ) : (1, []),
  
  # Indo para o estado final
  (1, '' , '$' ) : (2, ['$'])
} 
accepting = [2]

string = "aaabbb"

P = PDA(initial, edges, accepting)

print( P.accept(string) )




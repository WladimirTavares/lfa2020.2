# Pushdown automara 
# L = { ww^R | for all w \in (a+b)*}

# Context-Free Grammar
# S -> aSa | bSb | epsilon 


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
  
  #Empilhando w   
  (0, 'a', '$')  : (0, ['a','$']), 
  (0, 'b', '$')  : (0, ['b','$']),
  (0, 'a', 'a')  : (0, ['a','a']),
  (0, 'a', 'b')  : (0, ['a','b']),
  (0, 'b', 'a')  : (0, ['b','a']),
  (0, 'b', 'b')  : (0, ['b','b']),
  
  #não determinismo 
  (0, '', 'a')  : (1, ['a']),
  (0, '', 'b')  : (1, ['b']),
  (0, '', '$')  : (1, ['$']),
  
  #desimpilhando w^R  
  (1, 'a' , 'a' ) : (1, []),
  (1, 'b' , 'b' ) : (1, []),
  
  # Indo pro estado final
  (1, ''  , '$')  : (2, ['$'])

} 
accepting = [2]

string = "abba"

P = PDA(initial, edges, accepting)

print( P.accept(string) )




# A super classe Reg possui 5 classes filhas:
# * Epsilon()
# * Literal(a)
# * Or(r1,r2)
# * Concat(r1,r2)
# * Star(r1)

# A super classe Reg possui o método abstrato matches que recebe uma string
# devolve um valor booleano

# A expressão regular (a+b)*aa(a+b)* pode ser construída da seguinte maneira
#re1 = Literal("a") #a
#re2 = Literal("b") #b
#re3 = Or(re1, re2) #(a+b)
#re4 = Star(re3) # (a+b)*
#re5 = Concat( re4, Concat(re1,  Concat(re1, re4) ) ) # (a+b)*aa(a+b)*











class Reg: 
  def matches(w) -> bool:
    pass  
  

class Epsilon(Reg):
  def __init__(self):
    self.re1 = ""
      
  def __str__(self) -> str:
    return ""

  def matches(self, w) -> bool:
    return w == ""

class Literal(Reg):
  def __init__(self, a):
    self.re1 = a
    
  def __str__(self) -> str:
    return str(self.re1)    

  def matches(self, w) -> bool:
    return w == self.re1    


class Or(Reg):
  def __init__(self, re1, re2):
    self.re1 = re1
    self.re2 = re2    
        
  def __str__(self):
     return str(self.re1) + "+" + str(self.re2)

  def matches(self, w):
    return self.re1.matches(w) or self.re2.matches(w)


   
class Concat(Reg):
  def __init__(self, re1, re2):
    self.re1 = re1
    self.re2 = re2    
    

  def __str__(self):
    return str(self.re1) + str(self.re2)

  def matches(self, w):
    for pos in range( len(w) ):
      if self.re1.matches( w[0:pos] ) and self.re2.matches(w[pos:] ):
        return True
    return False
  


class Star(Reg):
  def __init__(self, re1):
    self.re1 = re1
    
  def __str__(self):
    return "(" + str(self.re1) + ")*"

  def matches(self, w):
    if w == "" :
      return True
    if len(w) == 1:
      return self.re1.matches(w)    
    else:
      for pos in range( 1, len(w) ):
        if self.re1.matches( w[0:pos] ) and self.matches(w[pos:] ):
          return True
      return False




re0 = Epsilon()
print (re0.matches(""))
print (re0)
re1 = Literal("a")
print (re1)
print (re1.matches("a"))
re2 = Literal("b")
print (re2)
re3 = Or(re1, re2)
print (re3.matches("a"))
print (re3.matches("b"))
re4 = Star(re3)
re5 = Concat( re4, Concat(re1,  Concat(re1, re4) ) )
print (re5)
print (re5.matches("babaababa"))





    

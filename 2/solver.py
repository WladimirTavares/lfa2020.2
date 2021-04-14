# Coloque aqui as transições do seu autômato
edges = {       
  (0, '0') : 1,
  (0, '1') : 5,
  (1, '0') : 6,
  (1, '1') : 2,
  (2, '0') : 3,
  (2, '1') : 6,
  (3, '0') : 4,
  (3, '1') : 6,
  (4, '0') : 6,
  (4, '1') : 6,
  (5, '0') : 1,
  (5, '1') : 6,
  (6, '0') : 6,
  (5, '1') : 6,




}

#Coloque aqui os estados finais do seu autômato
accepting = [0,1,3,5,6]

initial   = 0

# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in acceptingtermina em
    else:
        letter = string[0]
        remainder = string[1:]
        if (current, letter) in edges:
            newstate = edges[(current, letter)]
            return dfa(remainder, newstate, edges, accepting)
        return False


for i in range(5,30):
  string = "{0:b}".format(i)  
  print(">>>>>>>>")
  print(string)  
  print("========")
  print(dfa(string, initial, edges, accepting))    
  print("<<<<<<<<")


#string = input()
#print(dfa(string, initial, edges, accepting))

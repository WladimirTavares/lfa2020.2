# Strings binárias que começam ou terminam com 01
edges = { (0, 'a')  :  [1],
          (1, 'b')  :  [2],
          (2, 'b')  :  [2],
          (2, 'a')  :  [3],
          (3, 'a')  :  [4],
          (4, 'b')  :  [3],

          

}
initial   = 0
accepting = [3] 

def epsilon_nfa(string, current, edges, accepting): 
    #print ("current: " + str(current) + "string: " + string )    
    if string == "":
        return  current in accepting       
    else:
        if (current, '') in edges:
          for next in edges[(current,'')]:
            if epsilon_nfa(string, next, edges, accepting):
                    return True
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if epsilon_nfa(string[1:], next, edges, accepting):
                    return True
        
        return False

s = ""
translation = s.maketrans("01","ba")
        
for i in range(32,64):
  string = "{0:b}".format(i)  
  print(">>>>>>>>")
  string = string.translate(translation)  
  print(string) 
  print("========")
  print(epsilon_nfa(string, initial, edges, accepting))    
  print("<<<<<<<<")





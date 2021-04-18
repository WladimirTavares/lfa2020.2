# Autômato Finito Não-Determinístico para strings binárias em que 
# o penultimo dígito é 1

edges = {  (0,'0') : [0,1],
           (0,'1') : [0,3],
           (1,'0') : [2],
           (3,'1') : [4]
             
}
initial   =  0
accepting = [2,4] 

def nfa(string, current, edges, accepting): 
    if string == "":
        return  current in accepting        
    else:
        c = string[0]
        if (current,c) in edges:
            for next in edges[(current,c)]:
                if nfa(string[1:], next, edges, accepting):
                    return True
        return False
        

string = input()
print ( nfa(string, initial, edges, accepting) )



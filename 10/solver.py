# Autômato Finito Não-Determinístico para strings binárias em que 
# o penultimo dígito é 1

edges = {  (0,'0') : [1,3],
           (0,'1') : [3], 
           (1,'1') : [2],
           (2,'0') : [2],
           (2,'1') : [2],
           (3,'0') : [3,4],
           (3,'1') : [3],
           (4,'1') : [5],

 
             
}
initial   =  0
accepting = [2,5] 

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



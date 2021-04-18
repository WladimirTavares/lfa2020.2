# Autômato Finito Não-Determinístico para strings binárias em que 
# o penultimo dígito é 1

edges = {  (0,'0') : [0],
           (0,'1') : [0,1],
           (1,'0') : [2],
           (1,'1') : [2] 
}
initial   =  0
accepting = [2] 

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

#print( "Test case 1 passed: " + str(nfa("abc", 1, edges,accepting) == True) ) 
#print "Test case 2 passed: " + str(nfsmsim("aaa", 1, edges, accepting) == True) 
#print "Test case 3 passed: " + str(nfsmsim("abbbc", 1, edges, accepting) == True) 
#print "Test case 4 passed: " + str(nfsmsim("aabc", 1, edges, accepting) == False) 
#print "Test case 5 passed: " + str(nfsmsim("", 1, edges, accepting) == False) 


#
# For example, the regular expression r"a+|(?:ab+c)" might be encoded like
# this:
edges = { (1, 'a') : [2, 3],
          (1, '' ) : [4], 
          (2, 'a') : [2],
          (3, 'b') : [4, 3],
          (4, 'c') : [5] }
accepting = [2, 5] 

def epsilon_nfa(string, current, edges, accepting): 
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
        

        


print ("Test case 1 passed: " + str(epsilon_nfa("c", 1, edges, accepting) == True)) 
print ("Test case 2 passed: " + str(epsilon_nfa("aaa", 1, edges, accepting) == True)) 
#print "Test case 3 passed: " + str(nfsmsim("abbbc", 1, edges, accepting) == True) 
#print "Test case 4 passed: " + str(nfsmsim("aabc", 1, edges, accepting) == False) 
#print "Test case 5 passed: " + str(nfsmsim("", 1, edges, accepting) == False) 


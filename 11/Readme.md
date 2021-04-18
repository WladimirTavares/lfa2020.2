# Strings binárias que contêm pelos menos dois 0's ou exatamente dois 1's
Projete um autômato finito não-determinístico com transição epsilon que aceita a linguagem *L* das strings binárias que contêm  pelo menos dois 0's ou exatamente dois 1's. Por exemplo, 00,000,110 e 101 estão em *L* e 111, 0111 não está em *L*.

Utilize o código abaixo
```Python
# Strings binárias que começam ou terminam com 01
edges = { (0, '') :  [4,1],
          (1, '0') : [2], 
          (2, '1') : [3],
          (3, '0') : [3],
          (3, '1') : [3],
          (4, '0') : [4,5],
          (4, '1') : [4],       
          (5, '1') : [6]

 }
initial   = 0
accepting = [3, 6] 

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
        

string = input()
print (epsilon_nfa( string , initial, edges, accepting) )         

```

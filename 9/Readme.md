# Strings que contém a substring 00 
Projete um autômato finito não-determinístico que aceita a linguagem *L* das strings binárias que terminam em 00 ou 11. Por exemplo, 1000, 1010011 estão em *L* e 1010101101 não está em *L*.

Utilize o código abaixo
```Python
# Exemplo de NFA que aceita as strings binárias com o penúltimo dígito igual a 1
edges = {  (0,'0') : [0],
           (0,'1') : [0,1],
           (1,'0') : [2],
           (1,'1') : [2] 
}
initial   =  0 # estado inicial
accepting = [2] # conjunto de estado final

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

```

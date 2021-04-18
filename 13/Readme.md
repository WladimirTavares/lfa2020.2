# Todas Strings binárias exceto 01,101,0100 
Projete um autômato finito determinístico (DFA) que aceita a linguagem *L* de todas strings binárias exceto 01, 101, 0100. Por exemplo, 10, 010, 0101, 01000 estão em *L* e somente 01,101 e 0100 não está em *L*.

Utilize o código abaixo
```Python
# Coloque aqui as transições do seu autômato
edges = {
   (0,'0') : 1,            
}

#Coloque aqui os estados finais do seu autômato
accepting = []

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


string = input()
print(dfa(string, initial, edges, accepting))

```

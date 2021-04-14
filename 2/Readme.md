Projete um autômato finito determinístico que aceita a linguagem *L* de strings formada por 0's e 1's definida como:

<img src="https://latex.codecogs.com/svg.latex?L = \{ w | w \mbox{ tem } 011 \mbox{ como substring} \}">

Por exemplo, 0111 está em *L* e 0010 não está em *L*.

```Python
# Coloque aqui as transições do seu autômato
edges = {       
}

#Coloque aqui os estados finais do seu autômato
accepting = []

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


string = raw_input()
print dfa(string, 1, edges, accepting)
```

Projete um autômato finito determinístico que aceita a linguagem *L* das strings binárias que começam com 1 e que, quando interpretadas como números são múltiplos de 5. Por exemplo, *101, 1010, 1111* estão na linguagem; *100* e *111* não estão em L.

Dica 1: Use a idéia apresentada no vídeo utilizando 5 estados representando os restos da divisão por 5 e utilize um estado inicial que começa lendo o dígito 1.

Dica 2: Observe que o estado "morto" não precisa ser representado e nem a transição para ele.




```Python
# Coloque aqui as transições do seu autômato
edges = {       
}

#Coloque aqui os estados finais do seu autômato
accepting = []

# Função que roda o autômato
def dfa(string, current, edges, accepting):
    if string == "":
        return current in accepting
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

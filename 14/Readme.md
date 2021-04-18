# Linguagem definida pela expressão regular <!-- $$(ab)^*(ba)^*$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>

 
Projete um autômato finito determinístico (DFA) que aceita a linguagem definida pela seguinte expressão regular 

<!-- $$(ab)^*(ba)^*$$ --> 

<div align="center"><img style="background: white;" src="https://render.githubusercontent.com/render/math?math="></div>


Utilize o código Python abaixo
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

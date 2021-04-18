# coloque aqui a definição do seu autômato
edges = {(1, '1') : 2,
         (1, '0') : 1,
         (2, '0') : 1,
         (2, '1') : 3,
         (3, '0') : 3,
         (3, '1') : 3  
         }
accepting = [3]

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


string = input()
print(dfa(string, 1, edges, accepting))





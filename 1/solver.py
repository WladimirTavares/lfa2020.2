edges = {         
  (1,'0') : 2,
  (1,'1') : 1,
  (2,'0') : 2,
  (2,'1') : 3,
  (3,'0') : 2,
  (3,'1') : 4,
  (4,'0') : 2,
  (4,'1') : 1,
}
accepting = [4]

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





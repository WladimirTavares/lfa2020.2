edges = {         
  (0,'0') : 0,
  (0,'1') : 1,

  (1,'0') : 2,
  (1,'1') : 3,

  (2,'0') : 4,
  (2,'1') : 0,

  (3,'0') : 1,
  (3,'1') : 2,
  
  (4,'0') : 3,
  (4,'1') : 4,

  (5, '1'): 1,


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
print(dfa(string, 5, edges, accepting))





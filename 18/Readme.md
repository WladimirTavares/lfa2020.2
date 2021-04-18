# Expressão Regular 1
 
Uma expressão regular na linguagem Python pode ser escrita com o auxílio dos seguintes metacaracteres:

* Se `A` e `B` são expressões regulares então `A|B` é uma expressão regular que casa com `A` ou `B`

* Se `A` é uma expressão regular, a expressão regular `A*` casa com 0 ou mais repetições da lingugem da expressão regular A. Por exemplo, `ab*` casa com 'a', 'ab' ou a seguido de qualquer quantidade de b's.

* [] é usado para indicar um conjunto de caracteres. Por exemplo, '[amk]' casa com 'a','m' ou 'k'.

* `A{m,n}` é uma expressão regular que casa com m até n repetições da expressão regular A. Por exemplo, `a{1,2}` casa com 'a' e 'aa'.

* `A{m}` é uma expressão regular que casa com exatamente m repetições da expressão regular A. Por exemplo, `a{1,2}` casa com 'a' e 'aa'.

* `(...)` casa com toda expressão regular que esteja entre parênteses e indica e o fim de um grupo. O conteúdo do grupo pode sere recuperado depois de um casamento foi realizado. 

* `A|B` é uma expressão regular que casa com a expressão regular A ou B.

Por exemplo, a expressão regular `[01]*(00|11)[01]*` casa com todas as strings binárias com dois 0's consecutivos ou dois 1's consecutivos. 


Escreva uma expressão regular para o conjunto de strings sobre o alfabeto \{0,1\} cujo quarto símbolo a partir da extrema direita é 1.
 
Utilize o código Python abaixo
```Python
import re

string = input()

# Coloque aqui sua expressão regular
regexp = r'ab*'

print( re.fullmatch(regexp,string) != None  )

```

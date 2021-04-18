# Expressão Regular 1
 
Uma expressão regular na linguagem Python pode ser escrita com o auxílio dos seguintes metacaracteres:

* Se `A` e `B` são expressões regulares então `A|B` é uma expressão regular que casa com `A` ou `B`

* Se `A` é uma expressão regular, a expressão regular `A*` casa com 0 ou mais repetições da lingugem da expressão regular A. Por exemplo, `ab*` casa com 'a', 'ab' ou a seguido de qualquer quantidade de b's.

* [] é usado para indicar um conjunto de caracteres. Por exemplo, '[amk]' casa com 'a','m' ou 'k'.


Escreva uma expressão regular para o conjunto de strings sobre o alfabeto \{a,b,c\} que contém pelo menos um a e pelo menos um b.

Utilize o código Python abaixo
```Python
import re

string = input()

# Coloque aqui sua expressão regular
regexp = r'ab*'

print( re.fullmatch(regexp,string) != None  )

```

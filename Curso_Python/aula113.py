# Como importar seus próprios módulos:

from aula113_package.modulo import soma_modulo # Primeira forma de import
import aula113_package.modulo # Segunda forma de import
from aula113_package import modulo # Terceira forma de import
from aula113_package.modulo import * # Má prática, porém também é uma forma, o * importa TUDO que está dentro do módulo

# * = All, seleciona tudo no import, há como manipular isso, está dentro da pasta 113_package

print(soma_modulo(1, 2)) # Primeira forma
print(aula113_package.modulo.soma_modulo(1,2)) # Segunda forma
print(modulo.soma_modulo(1, 2)) # Terceira forma
print(variavel) # Quarta forma (má prática), funciona igual a primeira pois está importando tudo.
# print(nova_variavel) # Mesmo importando TUDO, eu não declarei no __all__ a "nova_variavel", então NÃO É POSSÍVEL USA-LA


"""
Iterando strings com while
"""
#         01234567891011
# nome = 'Rafael Ricardo'  # Iteráveis
#         121110987654321


nome = 'Rafael Ricardo '  # Iteráveis

indice = 0 # Declaro contador como zero
novo_nome = '' # Declaro a variável novo_nome como vazia para usar ela para armazenar o nome no while

while indice < len(nome): # Se meu indice for menor que o tamanho do nome...
    
    letra = nome[indice] # declaro a variável letra tendo como valor cada letra do nome, que seria o nome
    
    novo_nome += f'*{letra}' # Aqui eu declaro o valor da variável novo_nome que seria a variável letra e
    # incremento o * antes de cada letra e guardo dentro da variável nome
    
    indice += 1 # incremento do indice para fazer com todas as letras.


print(novo_nome) # Exibindo o nome completo com os * entre as letras
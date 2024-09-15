"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1 # Contador de linhas

while linha <= qtd_linhas:#Para cada linha, quero exibir 5 colunas, para isso irá ter um While dentro de outro
    # Para cada vez que o While de fora executa uma vez, o de dentro executa 5 vezes
    coluna = 1 # Contador de colunas
    while coluna <= qtd_colunas: 
        print(f'{linha=} {coluna=}')
        coluna += 1
        # Depois de ter realizado 5 vezes ele vai descer e somar +1 linha
    linha += 1


print('Acabou')
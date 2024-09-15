for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else não executará')
        break

    for j in range(1, 3): # limitando o range de colunas para 2, então ele vai printar a mesma linha duas vezes, para a coluna 1 e 2.
        print(i, j)
else: # Nesse caso esse else só vai aparecer se eu retirar o if == 8
    print('For completo com sucesso!')
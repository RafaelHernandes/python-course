# Exercício com if e comparação:

primeiro_valor = input("Digite o primeiro número: ")
segundo_valor = input("Digite o segundo número: ")

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor < int_segundo_valor:
    print(f"O segundo valor '{int_segundo_valor}' é maior que o primeiro valor '{int_primeiro_valor}'! ")
elif int_primeiro_valor > int_segundo_valor:
    print(f"O primeiro valor '{int_primeiro_valor}' é maior que o segundo valor '{int_segundo_valor}'! ")
elif int_primeiro_valor == int_segundo_valor:
    print(f"Os valores '{int_primeiro_valor}' e '{int_segundo_valor}' são iguais! ")
    

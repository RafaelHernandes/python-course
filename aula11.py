# Precedencia dos operadores

# 1. (n + n)  Primeiro executa-se os parenteses
# 2. **  Segundo a exponenciação
# 3. * / // %  Terceiro a multiplicação, divisão ou módulo
# 4. + - Quarto a soma e a subtração

conta_1 = 1 + 1 ** 5 + 5 # O resultado é 7, e a ideia era para ser 1024, seguindo os precedentes a veja a segunda conta abaixo:
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) # O Agora vai realizar as contas dos parenteses e depois exponenciar.
print(conta_2)
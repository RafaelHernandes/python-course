# isinstance() - para saber se objeto é de determinado tipo
lista = [
    "a", 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {"nome": "Luiz"},
]

for item in lista:
    if isinstance(item, set): # Variável a ser verificada, tipo de dado q vc está buscando "tipo set"
        item.add(5)
        print(item, isinstance(item, set))
        
    if isinstance(item, str): 
        print(item.upper(), isinstance(item, str))
        
    if isinstance(item, (int, float)): 
        print(item, item * 2)
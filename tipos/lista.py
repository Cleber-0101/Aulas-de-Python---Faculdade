
# Lista em Python 

numeros = [ 1,2,3,4,5,5]
print(type(numeros))
print(f'Os numeros desta lista são: {numeros}')

# Metodo de Adicionar , no final da lista 
numeros.append(10)
print(numeros)

# Metodo para saber o Tamanho da lista 
print(len(numeros))

# Alterar um dado da Lista, passando o INDEXADOR dele 
numeros[0] = 1000
print(numeros)

# Inserindo passando o indexados e um novo valor 
numeros.insert(0 , -3000)
print(numeros)
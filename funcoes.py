'''
x = int(input("Digite um numero inteiro maior que 0: "))
fat = x
while (x > 1):
    fat = fat * (x - 1)
    x = x - 1
print("Seu numero fatoriado: ", fat)
'''

'''
def calculo(x, y, z):
    adicao = x + y + z
    return adicao

def main():
    a = int(input("Digite um numero: "))
    b = int(input("Digite um numero: "))
    c = int(input("Digite um numero: ")) 

    result = calculo(a, b, c)
    result = result / 3
    print("A media dos 3 numeros é: ", result)
main()
'''

'''
def potencia(base, indice):
    potenciacao = base ** indice
    return potenciacao

def main():
    base = int(input("Digite a base: "))
    indice = int(input("Digite o indice: "))
    
    result = potencia(base, indice)
    print("O valor da Potencia é: ", result)
main()
'''

'''
def main():
    x = float(input("X: "))
    y = float(input("Y: "))
    a = int(input("A: "))
    b = int(input("B: "))
    print(potencia(x, a) + potencia(y, b) + potencia(x - y, a + b))

def potencia(base, expoente):
    i = 0
    pot = 1
    while i < expoente:
        pot *= base
        i += 1
    return pot
main()
'''    

'''
def main():
    A=cria_matriz()
    imprime_matriz(A)

def cria_matriz():
    n_linhas=int(input("Digite o numero de linhas: "))
    n_colunas=int(input("Digite o numero de colunas: "))
    matriz=[]
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            elemento = int(input(f"Digite o elemento para a posição [{i}][{j}]: "))
            linha.append(elemento)
        matriz.append(linha)   
    return matriz

def imprime_matriz(matriz):
    m=len(matriz)
    n=len(matriz[0])
    for i in range(m):
        for j in range(n):
            print("%6d" % (matriz[i][j]), end="")
        print()
main()
'''
def perm_paridade(lista):
    paridade = 1
    lista = lista[:]
    for i in range(0,len(lista) - 1):
        if lista[i] != i:
            paridade *= -1
            mn = lista[i+1:].index(min(lista[i+1:])) + i + 1
            lista[i],lista[mn] = lista[mn],lista[i]
    return paridade


def determinante_leibnitz(self):
    assert len(self) == len(self[0])
    dim = len(self)
    det,mul = 0,1
    for perm in permutacao([num for num in range(dim)]):
        for i in range(dim):
            mul *= self[i][perm[i]]
        det += perm_paridade(perm)*mul
        mul = 1
    return det

def perm_paridade(lista):
    paridade = 1
    lista = lista[:]
    for i in range(0,len(lista) - 1):
        if lista[i] != i:
            paridade *= -1
            mn = lista[i+1:].index(min(lista[i+1:])) + i + 1
            lista[i],lista[mn] = lista[mn],lista[i]
    return paridade

def permutacao(lista):
    if len(lista) <= 1:
        return [lista]
    templista = []
    for i in range(len(lista)):
        part = lista[:i] + lista[i+1:]
        for j in permutacao(part):
            templista.append(lista[i:i+1] + j)
    return templista

def matrizes():
    while True:
        print("Escolha entre as matrizes!")
        print("1 - Matriz 2x2")
        print("2 - Matriz 3x3")
        print("3 - Matriz 4x4")
        print("4 - Matriz 5x5")
        print("5 - Mais opções...")
        print("6 - Voltar")
        opt = int(input("Selecione entre as opções 1,2,3,4,5,6: "))
        if opt == 1:
            num1 = int(input("Digite o primeiro número da primeira linha: "))
            num2 = int(input("Digite o segundo número da primeira linha: "))
            num3 = int(input("Digite o primeiro número da segunda linha: "))
            num4 = int(input("Digite o segundo número da segunda linha: "))
            matriz = [[num1, num2], [num3, num4]]
            det = determinante_leibnitz(matriz)
            print("O resultado desta determinante é:", det)
            break
        if opt == 2:
            num1 = int(input("Digite o primeiro número da primeira linha: "))
            num2 = int(input("Digite o segundo número da primeira linha: "))
            num3 = int(input("Digite o terceiro número da primeira linha: "))
            num4 = int(input("Digite o primeiro número da segunda linha: "))
            num5 = int(input("Digite o segundo número da segunda linha: "))
            num6 = int(input("Digite o terceiro número da segunda linha: "))
            num7 = int(input("Digite o primeiro número da terceira linha: "))
            num8 = int(input("Digite o segundo número da terceira linha: "))
            num9 = int(input("Digite o terceiro número da terceira linha: "))
            matriz = [[num1, num2, num3], [num4, num5, num6], [num7, num8, num9]]
            det = determinante_leibnitz(matriz)
            print("O resultado desta determinante é:", det)
            break
        if opt == 3:
            num1 = int(input("Digite o primeiro número da primeira linha: "))
            num2 = int(input("Digite o segundo número da primeira linha: "))
            num3 = int(input("Digite o terceiro número da primeira linha: "))
            num4 = int(input("Digite o quarto número da primeira linha: "))
            num5 = int(input("Digite o primeiro número da segunda linha: "))
            num6 = int(input("Digite o segundo número da segunda linha: "))
            num7 = int(input("Digite o terceiro número da segunda linha: "))
            num8 = int(input("Digite o quarto número da segunda linha: "))
            num9 = int(input("Digite o primeiro número da terceira linha: "))
            num10 = int(input("Digite o segundo número da terceira linha: "))
            num11 = int(input("Digite o terceiro número da terceira linha: "))
            num12 = int(input("Digite o quarto número da terceira linha: "))
            num13 = int(input("Digite o primeiro número da quarta linha: "))
            num14 = int(input("Digite o segundo número da quarta linha: "))
            num15 = int(input("Digite o terceiro número da quarta linha: "))
            num16 = int(input("Digite o quarto número da quarta linha: "))
            matriz = [[num1, num2, num3, num4], [num5, num6, num7, num8], [num9, num10, num11, num12], [num13, num14, num15, num16]]
            det = determinante_leibnitz(matriz)
            print("O resultado desta determinante é:", det)
            break
        if opt == 4:
            num1 = int(input("Digite o primeiro número da primeira linha: "))
            num2 = int(input("Digite o segundo número da primeira linha: "))
            num3 = int(input("Digite o terceiro número da primeira linha: "))
            num4 = int(input("Digite o quarto número da primeira linha: "))
            num5 = int(input("Digite o quinto número da primeira linha: "))
            num6 = int(input("Digite o primeiro número da segunda linha: "))
            num7 = int(input("Digite o segundo número da segunda linha: "))
            num8 = int(input("Digite o terceiro número da segunda linha: "))
            num9 = int(input("Digite o quarto número da segunda linha: "))
            num10 = int(input("Digite o quinto número da segunda linha: "))
            num11 = int(input("Digite o primeiro número da terceira linha: "))
            num12 = int(input("Digite o segundo número da terceira linha: "))
            num13 = int(input("Digite o terceiro número da terceira linha: "))
            num14 = int(input("Digite o quarto número da terceira linha: "))
            num15 = int(input("Digite o quinto número da terceira linha: "))
            num16 = int(input("Digite o primeiro número da quarta linha: "))
            num17 = int(input("Digite o segundo número da quarta linha: "))
            num18 = int(input("Digite o terceiro número da quarta linha: "))
            num19 = int(input("Digite o quarto número da quarta linha: "))
            num20 = int(input("Digite o quinto número da quarta linha: "))
            num21 = int(input("Digite o primeiro número da quinta linha: "))
            num22 = int(input("Digite o segundo número da quinta linha: "))
            num23 = int(input("Digite o terceiro número da quinta linha: "))
            num24 = int(input("Digite o quarto número da quinta linha: "))
            num25 = int(input("Digite o quinto número da quinta linha: "))
            matriz = [[num1, num2, num3, num4, num5], [num6, num7, num8, num9, num10], [num11, num12, num13, num14, num15], [num16, num17, num18, num19, num20], [num21, num22, num23, num24, num25]]
            det = determinante_leibnitz(matriz)
            print("O resultado desta determinante é:", det)
            break
        if opt == 5:
            print("Eu só fiz esses menus pra passar tempo (e sei que existem formas mais fáceis de executar isso), Se não quiser utilizar para testar matrizes maiores, basta abrir o código sem menus descriminado na pasta.")
            break
        if opt == 6:
            break
        else:
            print("Erro, você fez cagada... Escolhe um número nas opções ai!")
            break

#comentar isto caso não queria utilizar os menu's
while True:
    print("Resolvedor de matrizes 10000, o mais potente do mercado 😎")
    print("Escolha entre as opções")
    print("1 - Matrizes")
    print("2 - Sair")
    op = int(input("Escolha entre as opções 1 e 2: "))
    if op == 1:
        matrizes()
    elif op == 2:
        break
    else:
        print("Escolha entre as opções validas!")



#Jeito normal de se fazer, descomente e comente os menus para retirar a função
#matriz = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
#det = determinante_leibnitz(matriz)
#print("O resultado desta determinante é:", det)
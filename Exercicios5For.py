
from time import sleep
import playsound
import math
from datetime import datetime

def contagem_regressiva():
    for n in range(10, 0, -1):
        print(n)
        sleep(1)
    playsound.playsound("fogos.mp3")
    print("KABUM! KATCHAU!")


def contagem_pares():
    for n in range(1, 51):
        if n % 2 == 0:
         print (n, end=" ")

def impar_multiplo_3():
    soma = 0
    cont = 0
    for n in range(1, 501):
        if n % 2 != 0 and n % 3 == 0:
            cont += 1
            soma = soma + n
    print(" A soma dos {} números é igual a {}".format(cont, soma))

def tabuada_ver2():
    num = int(input("Digite um numero para ver a sua tabuada: "))
    print("-=-" * 20)
    for c in range (0, 11):
        res = num * c
        print("{} X {} = {}".format(num, c, res))

def soma_pares():
    posicao = ("primeiro", "segundo", "terceiro", "quarto", "quinto", "sexto")
    pos = - 1
    soma = 0
    for n in range(1, 7):
        pos += 1
        num = int(input("Digite o {} valor: ".format(posicao[pos])))
        if num % 2 == 0:
            soma = soma + num
    print("A soma dos valores citados é {}".format(soma))

def progressao_aritmetica():
    print("=" * 40)
    print("PROGRESSÃO ARITMÉTICA")
    print("=" * 40)

    a1 = int(input("Digite o 1° termo: "))
    n = int(input("Digite a quantidade de termos: "))
    r = int(input("Digite a razão: "))
    n2 = 0

    for c in range(0, n):
        n2 += 1
        res = a1 + (n2 - 1) * r
        print(res, end=" - ")
    print("IT'S OVER")

def numeros_primos():
    num = int(input("Digite um número para verificar se é primo: "))
    contador = 0

    for i in range(1, num  + 1):
        if num % i == 0:
            contador += 1
            print("\033[34m", end=" ")
        else:
            print("\033[31m", end=" ")
        print("{} ".format(i), end=" ")
    if contador == 2:
        print(" O número {} é PRIMO".format(num))
    else:
        print("O número {} NÃO É PRIMO".format(num))

def palindromo():
    frase = str(input("Digite uma frase: ")).strip().upper()
    palavras = frase.split()
    junto = "".join(palavras)
    inverso = ""
    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]

    print(" Você digitou a frase: {}".format(junto))
    print(" Essa frase invertida é: {}".format(inverso))
    if inverso == junto:
        print("Essa frase é um PALINDROMO")
    else:
        print("Essa frase NÃO É um PALINDROMO")

def maioridade():
    pos = 1
    dt = datetime.now()
    ano_atual = dt.year
    menor_idade = 0
    maior_idade = 0
    for i in range(0,7):
        idade = int(input("Em que ano nasceu a {}° pessoa? ".format(pos)))
        pos += 1
        if ano_atual - idade >= 18:
            maior_idade += 1
        else:
            menor_idade += 1
    print("Ao todo tivemos {} pessoas maiores de idade".format(maior_idade))
    print("E também tivemos {} pessoas de menores".format(menor_idade))

def menor_maior_peso():
    pos = 1
    lista_pesos = []
    for i in range(1, 7):
        peso = float(input("Digite o peso da {}° pessoa: ".format(pos)))
        pos += 1
        lista_pesos.append(peso)
    lista_pesos.sort()
    print("O maior peso lido foi de {} kg".format(max(lista_pesos)))
    print("O menor peso lido foi de {} kg".format(min(lista_pesos)))

def analisador():
    idtotal = 0
    maioridadehomem = 0
    nomevelho = ""
    cont_m = 0
    for i in range(1, 5):
        print("----- {}° PESSOA -----".format(i))

        nome = str(input("Nome: ")).strip()
        idade = int(input("Idade: "))
        sexo = str(input("Sexo [M/F]: ")).strip().upper()
        idtotal += idade
        if i == 1 and sexo in "M":
            maioridadehomem = idade
            nomevelho = nome
        if sexo in "M" and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = nome
        if sexo in "F" and idade <= 20:
            cont_m += 1

    idmedia = idtotal / 4
    print("A média de idade do grupo é de {} anos".format(idmedia))
    print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
    print("Neste grupo {} mulheres têm menos de 20 anos".format(cont_m))












if __name__ == "__main__":
    #contagem_regressiva()
    #contagem_pares()
    #impar_multiplo_3()
    #tabuada_ver2()
    #soma_pares()
    #progressao_aritmetica()
    #numeros_primos()
    #palindromo()
    #maioridade()
    #menor_maior_peso()
    analisador()


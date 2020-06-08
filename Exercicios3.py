from datetime import date
import random
import playsound
from time import sleep


def jogo_adivinhacao():
    print("-=-" * 20)
    num = int(input("Digite um numero que eu tentarei adivinhar, você tem 20% de chance de ganhar: "))
    print("-=-" * 20)
    n = random.randint(0, 5)
    print("PROCESSANDO...")
    sleep(1.5)

    if(num == n):
        print("Parabéns você é vidente. Eu pensei no numero {}".format(n))
        playsound.playsound("acertou.mp3")
        print("-=-" * 20)

    else:
        print("Você errou, eu pensei no número {} e você no {}".format(n, num))
        playsound.playsound("errou.mp3")
        print("-=-" * 20)

def radar():
    print("-=-" * 20)
    velocidade = float(input("Qual a velocidade atual do carro? "))
    multa = (velocidade - 80) * 7
    print("-=-" * 20)

    if(velocidade < 80):
        print("Tenha um bom dia! Dirija com segurança!")
        print("-=-" * 20)

    else:
        print("MULTADO MALUCO! Você ultrapassou a velocidade máxima de 80km/h e receberá uma multa de R${:.2f}".format(multa))
        print("-=-" * 20)

def par_impar():
    print("-=-" * 20)
    num = (float(input("Digite um número qualquer: ")))
    c = num % 2
    print("-=-" * 20)

    if(c == 0):
        print("O número {} é PAR".format(num))
    else:
        print("O número {} é IMPAR".format(num))

def viagem():
    km = int(input("Qual é a distância da sua viagem? "))
    c1 = km * 0.5
    c2 = km * 0.45

    if(km >= 200):
        print("Sua viagem irá custar R$ {:.2f}".format(c2))
    else:
        print("Sua viagem irá custar R$ {:.2f}".format(c1))

def bissexto():
    ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
    if (ano == 0):
        ano = date.today().year
    if (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
        print("O ano {} é BISSEXTO".format(ano))
    else:
        print("O ano {} NÃO é BISSEXTO".format(ano))

def maior_menor():
    a = int(input("Primeiro valor: "))
    b = int(input("Segundo valor: "))
    c = int(input("Terceiro valor: "))
# Verificando menor
    menor = a
    if b < a and b < c:
        menor = b
    if c < a and c < b:
        menor = c

    print("O menor valor é {}".format(menor))

# Verificando maior
    maior = b
    if a > b and a > c:
        maior = a
    if c > b and c > a:
        maior = c

    print("O maior valor é {}".format(maior))

def aumento_multiplo():
    salario = float(input("Digite o seu salário: "))
    r1 = salario + (salario * (10/100))
    r2 = salario + (salario * (15/100))
    if(salario > 1250):
        print("Seu salário é de R$ {} e com o reajuste será R${:.2f}".format(salario, r1))
    else:
        print("Seu salário é de R$ {} e com o reajuste será R${:.2f}".format(salario, r2))

def analise_triangulo():
    print("-=-" * 20)
    print("Analisador de triângulos")
    print("-=-" * 20)
    a = float(input("Digite o primeiro segmento: "))
    b = float(input("Digite o segundo segmento: "))
    c = float(input("Digite o terceiro segmento: "))

    if a < b + c and b < a + c and c < a + b:
        print("Com os segmentos digitados você pode construir um triângulo!")
    else:
        print("Com os segmentos digitados você não pode construir um triângulo")

    print("-=-" * 20)


if __name__ == "__main__":
    #jogo_adivinhacao()
    #radar()
    #par_impar()
    #viagem()
    #bissexto()
    #maior_menor()
    #aumento_multiplo()
    analise_triangulo()
import math
import random
def cortador_de_numeros():
    num = float(input("Digite um valor: "))
    print("O valor digitado foi {}, e sua parte inteira é {}".format(num, math.trunc(num)))

def cateto():
    catops = float(input("Qual o valor do cateto oposto? "))
    catadj = float(input("Qual o valor do cateto adjacente? "))
    hi = math.hypot(catops, catadj)
    print("O valor da hipotenusa é: {:.2f}".format(hi))

def sen_cos_tg():
    angulo = float(input("Digite o angulo que deseja: "))
    conv = math.radians(angulo)

    sen = math.sin(conv)
    print("O angulo de {} tem o SENO de {:.2f}".format(angulo, sen))

    cos = math.cos(conv)
    print("O angulo de {} tem o COSSENO de {:.2f}". format(angulo, cos))

    tg = math.tan(conv)
    print("O angulo de {} tem a TANGENTE de {:.2f}".format(angulo, tg))

def sorteador():
    n1 = str(input("Nome do primeiro aluno: "))
    n2 = str(input("Segundo aluno: "))
    n3 = str(input("Terceiro aluno: "))
    n4 = str(input("Quarto aluno: "))
    lista = [n1, n2, n3, n4]
    escolhido = random.choice(lista)
    print("O sorteado é {}".format(escolhido))

def sortea_ordem():
    n1 = str(input("Primeiro aluno: "))
    n2 = str(input("Segundo aluno: "))
    n3 = str(input("Terceiro aluno: "))
    n4 = str(input("Quarto aluno: "))
    lista = [n1, n2, n3, n4]
    random.shuffle(lista)
    print("A ordem de apresentação será {}".format(lista))

def analisador_de_textos():
    nome = str(input("Digite seu nome completo: ")).strip()
    print("Analisando seu nome... ")
    print("Seu nome em maiusculas é {}".format(nome.upper()))
    print("Seu nome em minusculas é {}".format(nome.lower()))
    print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(" ")))
    print("Seu primeiro nome tem {} letras".format(nome.find(" ")))

def separador():
    num = int(input("Digite um número "))
    u = num // 1 % 10
    d = num // 10 % 10
    c = num // 100 % 10
    m = num // 1000 % 10
    print("Analisando o número {}".format(num))
    print("Unidade: {}".format(u))
    print("Dezena: {}".format(d))
    print("Centena: {}".format(c))
    print("Milhar: {}".format(m))

def nome_cidade():
    c = str(input("Digite uma cidade: ")).upper().strip().split()
    print("Essa cidade tem SANTO no nome? {}".format("SANTO" in c[0]))

def analise():
    nome = str(input("Digite seu nome completo: ")).strip().upper().split()
    print("Seu nome tem Silva? {}".format("SILVA" in nome))

def ocorrencia_crct():
    frase = str(input("Digite uma frase: ")).upper().strip()
    print("A letra A apareceu {} vezes".format(frase.count("A")))
    print("A letra A aparece pela primeira vez em {}".format(frase.find("A")+ 1))
    print("A letra A aparece pela ultima vez na posição {}".format(frase.rfind("A")))

def analise_de_nome():
    nome = str(input("Digite seu nome completo: ")).strip().split()
    print("Seu primeiro nome é {}".format(nome[0]))
    print("Seu ultimo nome é {}".format(nome[-1]))


if __name__ == "__main__":
    #cortador_de_numeros()
    #cateto()
    #sen_cos_tg()
    #sorteador()
    #sortea_ordem()
    #analisador_de_textos()
    #separador()
    #nome_cidade()
    #analise()
    #ocorrencia_crct()
    analise_de_nome()

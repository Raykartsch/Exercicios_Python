
from time import sleep
from datetime import datetime
import math
import random
import playsound

def emprestimo():
    print("-=-" * 20)
    casa = float(input("Qual é o valor da casa? R$"))
    salario = float(input("Qual é o seu salário? R$ "))
    anos = int(input("Quantos anos de financiamento? "))
    prestação = casa / (anos * 12)
    minimo = salario * 30/100
    print("Para pagar uma casa de R$ {:.2f} em {} anos".format(casa, anos))
    print("A prestação será de R$ {:.2f}".format(prestação))
    if(prestação <= minimo):
        print("Empréstimo DEFERIDO!")
    else:
        print("Empréstimo INDEFERIDO!")
    print("-=-" * 20)

def conversor_numerico():
    num = int(input("Digite um número inteiro: "))
    print('''Escolha uma das bases para converter: 
    [ 1 ] converter para BINÁRIO
    [ 2 ] converter para OCTAL
    [ 3 ] converter para HEXADECIMAL''')
    opcao = int(input("Sua opção: "))

    print("PROCESSANDO...")
    sleep(1)

    if opcao == 1:
        print("O número {} convertido para BINÁRIO é igual a {}".format(num, bin(num)))
    elif opcao == 2:
        print("O número {} convertido para OCTAL é igual a {}".format(num, oct(num)))
    elif opcao == 3:
        print("O número {} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)))
    else:
        print("Digite um número entre 1 e 3 para realizar a conversão!")

    print("PROCESSAMENTO CONCLUÍDO!")

def comparar_numeros():
    n1 = float(input("Digite o primeiro valor: "))
    n2 = float(input("Digite o segundo valor: "))
    if n1 > n2:
        print("O PRIMEIRO número é maior")
    elif n2 > n1:
        print("O SEGUNDO número é maior")
    else:
        print("Não existe número maior, os dois são IGUAIS")

def alistamento_militar():
     nasc = int(input("Digite seu ano de nascimento: "))
     dt = datetime.now()
     anoatual = dt.year
     idade = anoatual - nasc
     print("Quem nasceu em {} tem {} em {}".format(nasc, idade, anoatual))

     if idade > 18 :
         saldo = idade - 18
         p_ano = anoatual - saldo
         print("Apresente-se à junta militar IMEDIATAMENTE.")
         print("Faz {} ano(s) que você deveria ter se apresentado para as forças armadas!".format(saldo))
         print("Seu alistamento foi em {}".format(p_ano))

     elif idade == 18:
         print('''Você deve se apresentar à junta militar NESTE ANO!''')

     elif idade < 18:
         saldo = 18 - idade
         f_ano = anoatual + saldo
         print("Atualmente você tem {} anos e deve se apresentar daqui {} anos.\nSeu alistamento será em {}.".format(idade, saldo, f_ano))

def classico_media():
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    media = (n1 + n2) / 2
    print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, media))

    if media >= 7:
        print("O aluno está APROVADO")
    elif media >= 4:
        print("O aluno está em RECUPERAÇÃO")
    else:
        print("O aluno está REPROVADO")

def classificacao_atleta():
    ano = int(input("Digite o ano de nascimento do atleta: "))
    dt = datetime.now()
    ano_atual = dt.year
    idade = ano_atual - ano
    print("O atleta tem {} anos".format(idade))

    if idade <= 9:
        print("Classificação: MIRIM")
    elif idade <= 14:
        print("Classificação: INFANTIL")
    elif idade <= 19:
        print("Classificação: JUNIOR")
    elif idade <= 25:
        print("Classificação: SÊNIOR")
    else:
        print("Classificação: MASTER")

def formacao_triangulo():
    a = int(input("Digite o primeiro segmento: "))
    b = int(input("Digite o segundo segmento: "))
    c = int(input("Digite o terceiro segmento: "))
    if a < b + c and b < a + c and c < a + b:
        print("Os segmentos acima podem formar um triângulo ", end='')
        if a == b == c:
            print("EQUILÁTERO!")
        elif a != b != c != a:
            print("ESCALENO!")
        else:
            print("ISÓSCELES")
    else:
        print("Os segmentos acima NÃO podem formar um triângulo!")

def calculo_imc():
    peso = float(input("Qual o seu peso? (kg) "))
    altura = float(input("Qual a sua altura? (m) "))
    imc = peso / (altura ** 2)
    print("O seu IMC é {:.2f}".format(imc))
    if imc <= 18.5:
        print("Você está abaixo do peso recomendado!")
    elif imc <= 24.9:
        print("Você está com peso ideal!")
    elif imc <= 29.9:
        print("Você está com sobrepeso!")
    elif imc <= 39.9:
        print("Você está com obesidade!")
    elif imc > 40:
        print("Você está com obesidade mórbida!")

def gerenciador_pagamentos():
    print("-=-" * 20)
    preco = int(input("Digite o valor das compras: R$ "))
    print('''FORMAS DE PAGAMENTO
    [ 1 ] à vista dinheiro/cheque - 10% de desconto
    [ 2 ] à vista cartão - 5% de desconto
    [ 3 ] 2x no cartão 
    [ 4 ] 3x ou mais no cartão''')
    opcao = int(input("Qual é a escolha de pagamento? "))
    if opcao == 1:
        total = preco - (preco * 0.90)
        print("Sua compra de {:.2f} vai lhe custar {:.2f} à vista com o desconto de 15%".format(preco, total))
    elif opcao == 2:
        total = preco - (preco * 0.95)
        print("Sua compra de R${:.2f} vai lhe custar R${:.2f} à vista no cartão com o desconto de 5%".format(preco, total))
    elif opcao == 3:
        total = preco / 2
        print("Sua compra de R$ {:.2f} em 2x no cartão ficará R$ {:.2f}".format(preco, total))
    elif opcao == 4:
        parcelas = int(input("Quantas parcelas? "))
        valorfinal = preco * (1 + ((20/100) * parcelas))
        print("Sua compra de R$ {:.2f} parceladas em {}x no cartão ficará R$ {:.2f}".format(preco, parcelas, valorfinal))
    else:
        print("OPÇÃO INVÁLIDA. Tente novamente!")

def pedra_papel_tesoura():
    print("-=-" * 20)
    print('''Suas opções:
    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    ''')
    jogador = int(input("Qual é a sua jogada? "))
    itens = ("PEDRA", "PAPEL", "TESOURA")
    pc = random.randint(0, 2)


    if jogador != 0 and jogador != 1 and jogador != 2:
        print("Opção INVÁLIDA. Digite novamente!")

    else:

        playsound.playsound("paper-scisor (1).mp3")
        print("JANKENGUU!!!")
        print("-=-" * 20)

        print("Você jogou {}".format(itens[jogador]))
        print("A máquina jogou {}".format(itens[pc]))
        print("-=-" * 20)
        if pc == 0:  # COMPUTADOR JOGOU PEDRA
            if jogador == 0:
                print("EMPATE!")
            elif jogador == 1:
                print("A máquina VENCEU!")
            elif jogador == 2:
                print("O jogador VENCEU!")
            else:
                print("JOGADA INVÁLIDA!")

        elif pc == 1:  # COMPUTADOR JOGOU PAPEL
            if jogador == 0:
                print("A máquina VENCEU!")
            elif jogador == 1:
                print("EMPATE!")
            elif jogador == 2:
                print("O jogador VENCEU!")
            else:
                print("JOGADA INVÁLIDA!")

        elif pc == 2:  # COMPUTADOR JOGOU TESOURA
            if jogador == 0:
                print("O jogador VENCEU!")
            elif jogador == 1:
                print("A máquina VENCEU!")
            elif jogador == 2:
                print("EMPATE!")
            else:
                print("JOGADA INVÁLIDA!")

    print("-=-" * 20)




if __name__ == "__main__":
    #emprestimo()
    #conversor_numerico()
    #comparar_numeros()
    #alistamento_militar()
    #classico_media()
    #classificacao_atleta()
    #formacao_triangulo()
    #calculo_imc()
    #gerenciador_pagamentos()
    pedra_papel_tesoura()
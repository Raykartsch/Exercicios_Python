import random
import playsound
from time import sleep
from math import factorial

def validacao_dados():
    s = str(input("Informe seu sexo: [M/F] ")).upper().strip()
    while s not in "MF":
        s = str(input("Dados inválidos. Informe seu sexo: [M/F] ")).upper().strip()
    print("Sexo {} registrado com sucesso!".format(s))

def jogo_adivinhacao_ver2():
    n = random.randint(0, 10)
    print("Acabei de pensar em número entre 1 e 10.")
    num = int(input("Qual o seu palpite? "))
    palpites = 1

    while num != n:
        playsound.playsound("errou.mp3")
        if n > num:
            num = int(input("ERROU! Mais... Tente novamente: "))
        elif n < num:
            num = int(input("ERROU! Menos... Tente novamente: "))
        palpites += 1
    playsound.playsound("acertou.mp3")
    print("ACERTOU! Você deu {} palpites e o número que eu pensei foi {}!".format(palpites, n))

def menu_opcoes():
    v1 = int(input("Digite o primeiro valor: "))
    v2 = int(input("Digite o segundo valor: "))
    sair = False
    while sair != True:
        print("=" * 60)
        print('''[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números\n[ 5 ] sair do programa''')
        print("=" * 60)
        opcao = int(input(">>>>>Qual é a sua opção? "))
        print("=" * 60)

        if opcao == 1: # SOMA
            soma = v1 + v2
            print("A soma de {} e {} é igual a {}".format(v1, v2, soma))

        elif opcao == 2: # MULTIPLICAR
            multi = v1 * v2
            print("A multiplicação de {} e {} é igual a {}".format(v1, v2, multi))

        elif opcao == 3: # MAIOR OU MENOR
            if v1 > v2:
                print("O número {} é maior que {}".format(v1, v2))
            elif v2 > v1:
                print("O número {} é maior que {}".format(v2, v1))
            elif v1 == v2:
                print("Os números {} e {} são iguais".format(v1, v2))

        elif opcao == 4: # NOVOS NUMEROS
            v1 = int(input("Redigite o primeiro valor: "))
            v2 = int(input("Redigite o segundo valor: "))

        elif opcao == 5: # ENCERRAR PROGRAMA
            print("ENCERRANDO O PROGRAMA...")
            sleep(0.5)
            sair = True

        else:
            print("Opção inválida. Digite um comando novamente: ")

    print("PROGRAMA ENCERRADO! VOLTANDO PARA ÁREA DE TRABALHO")

def fatorial(): #TESTAR FAZER COM O FOR
    num = int(input("Digite um número para calcular o seu fatorial: "))
    c = num
    fatorial = 1
    print("{}! = ".format(num), end=" ")
    while c > 1:
        fatorial *= c
        print("{} X".format(c), end=" ")
        c -= 1
    print("1 = {}".format(fatorial))

def progressaoaritmetica_ver2():
    print("=" * 30)
    print("PROGRESSÃO ARITMÉTICA")
    print("=" * 30)

    a1 = int(input("Digite o 1° termo: "))
    n = int(input("Digite a quantidade de termos: "))
    r = int(input("Digite a razão: "))
    n2 = 0

    while n2 != n:
        n2 += 1
        res = a1 + (n2 - 1) * r
        print(res, end=" - ")
    print("IT'S OVER")

def progressaoaritmetica_ver3():
    print("=" * 30)
    print("PROGRESSÃO ARITMÉTICA")
    print("=" * 30)

    a1 = int(input("Digite o 1° termo: "))
    n = int(input("Digite a quantidade de termos: ")) - 1
    r = int(input("Digite a razão: "))
    n2 = 0
    mais = 1
    cont = 0
    while mais != 0:
        n += mais
        while n2 < n:
            n2 += 1
            res = a1 + (n2 - 1) * r
            print(res, end=" - ")
            cont += 1
        print("PAUSA")
        mais = int(input("Quantos termos você quer mostrar a mais? "))
    print("Ao todo {} termos foram mostrados".format(n))
    print("IT'S OVER")

def sequencia_fibonacci():
    print("-" * 30)
    print("SEQUÊNCIA DE FIBONACCI")
    print("-" * 30)
    num = int(input("Quantos termos você quer mostrar?"))
    n1 = 0
    n2 = 1
    print("{} - {}".format(n1, n2), end="")
    cont = 3
    while cont <= num:
        n3 = n1 + n2
        print(" - {}".format(n3), end="")
        n1 = n2
        n2 = n3
        cont += 1
    print(" - FIM")

def tratando_valores():
    num = 0
    cont = 0
    soma = 0
    num = int(input("Digite um número [999 para parar]: "))
    while num != 999:
        soma += num
        cont += 1
        num = int(input("Digite um número [999 para parar]: "))
    print("Você digitou {} números e a soma entre eles foi {}".format(cont, soma))

def maior_menor_valores(): # BUGADO CONSERTAR DEPOIS - REFAZER
    cont = True
    contador = 0
    total = 0
    maior_valor = 0
    menor_valor = 0

    while cont == True:
        num = int(input("Digite um número: "))
        answer = str(input("Quer continuar? [S/N] ")).strip()

        if maior_valor < num:
            maior_valor = num
        elif menor_valor < num:
            menor_valor = num

        if answer in "Ss":
            contador += 1
            total += num

        elif answer in "Nn":
            contador += 1
            total += num
            cont = False
            media = total / contador
            print(f"Você digitou {contador} números e a média foi {media}")
            print(f"O maior valor foi {maior_valor} e o menor foi {menor_valor}")

        elif answer not in "SsNn":
            print("Resposta incorreta. Responda novamente")

def tratando_valores2():
    num = int(input("Digite um numero [999 para parar]: "))
    cont = 0
    soma = 0

    while num != 999:
        num = int(input("Digite um numero [999 para parar]: "))
        if num == 999:
            break
        cont += 1
        soma += num
    print(f"Você digitou {cont} números e a soma foi {soma}")

def tabuada_ver3():
    num = int(input("Digite um número para ver a sua tabuada: "))
    cont = 0
    res = 0
    while cont != 11:
        res = num * cont
        print(f"{num} X {cont} = {res}")
        cont += 1
        if cont == 11:
            print("-" * 40)
            num = int(input("Deseja ver tabuada de qual valor? "))
            print("-" * 40)
            if num >= 1:
                cont = 0
            else:
                break
    print("PROGRAMA TABUADA ENCERRADO!")

def par_impar():
    print("-" * 40)
    print("PAR ou IMPAR")
    print("-" * 40)
    cont = 0

    while True:
        jogador = int(input("Digite um número: "))
        while jogador not in range(0, 11):
            jogador = int(input("Digite um número entre 0 e 10: "))

        escolha = str(input("PAR ou ÍMPAR [P/I] ")).strip()
        while escolha not in "PpIi":
            escolha = str(input("PAR ou ÍMPAR [P/I]: ")).strip()

        computador = random.randint(0, 10)
        soma = jogador + computador
        res = ""

        #DEFINE O RESULTADO COMO PAR OU IMPAR
        if soma % 2 == 0:
            res = "PAR"
        else:
            res = "IMPAR"

        # RESULTADO DA BATALHA
        print("-" * 40)
        print(f"Você jogou {jogador} e o computador {computador}. Total de {soma} DEU {res}")
        print("-" * 40)

        if escolha in "Pp" and soma % 2 == 0:
            cont += 1
            print("-" * 40)
            print("Você VENCEU! Vamos jogar novamente...")

        elif escolha in "Ii" and soma % 2 != 0:
            cont += 1
            print("-" * 40)
            print("Você VENCEU! Vamos jogar novamente...")

        else:
            print("Você PERDEU!")
            break

    print(f"GAME OVER! Você venceu {cont} vezes")

def analise_dados_grupo():
    cont_idade = 0
    cont_masc = 0
    cont_mulheres = 0
    while True:
        print("-" * 40)
        print("CADASTRE UMA PESSOA")
        print("-" * 40)

        idade = int(input("Idade: "))
        while idade < 0:
            idade = int(input("Opção inválida. Idade: "))

        #Total de pessoas com mais de 18 anos
        if idade >= 18:
            cont_idade += 1

        sexo = str(input("Sexo [M/F]: "))
        while sexo not in "MmFf":
            sexo = str(input("Opção inválida. Sexo [M/F]: "))

        #Homens cadastrados
        if sexo in "Mm":
            cont_masc += 1

        # Mulheres com menos de 20 anos
        if sexo in "Ff" and idade <= 20:
            cont_mulheres += 1

        print("-" * 40)
        escolha = str(input("Continuar? [S/N] "))
        while escolha not in "SsNn":
            escolha = str(input("Opção inválida. Continuar? [S/N] "))

        if escolha in "Nn":
            break

    print(f"Total de pessoas com mais de 18 anos: {cont_idade}")
    print(f"Ao todo temos {cont_masc} homens cadastrados")
    print(f"E temos {cont_mulheres} mulheres com menos de 20 anos")


def estatisticas_produtos():
    print("-" * 40)
    print("LOJA ATACADÃO 2000")
    print("-" * 40)

    soma = cont_mil = menor = cont = 0
    menor_produto = ""

    while True:
        nome_produto = str(input("Nome do produto: ")).strip()

        preco = float(input("Preço: R$ "))
        cont += 1
        soma += preco

        #Invalidar valores negativos
        while preco < 0:
            preco = float(input("Digite um preço válido. Preço: R$ "))
        #Detectar preços maiores que mil
        if preco >= 1000:
            cont_mil += 1
        #Detectar o menor preço e seu respectivo produto
        if cont == 1 or preco < menor:
            menor = preco
            menor_produto = nome_produto

        #Esquema de escolha de continuação
        print("-" * 40)
        escolha = str(input("Quer continuar? [S/N] "))[0]
        print("-" * 40)
        while escolha not in "SsNn":
            escolha = str(input("Opção inválida. Continuar? [S/N] "))[0]
        if escolha in "Nn":
            break
    print("---------- FIM DO PROGRAMA ---------- ")
    print(f"O total da compra foi R${soma:.2f}")
    print(f"Você tem {cont_mil} produtos custando mais de R$ 1.000.00. Muito burguês")
    print(f"O produto mais barato foi {menor_produto} que custa R$ {menor:.2f}")

def caixa_eletronico(): #Tentar refazer de outro jeito, muito díficil essa bosta
    print("=" * 40)
    print("{:^40}".format("BANCO"))
    print("=" * 40)

    valorSaque = int(input("Que valor você quer sacar? R$ "))
    lista = [50, 20, 10, 1]
    cont = 0

    while True:
        # Se o valor de saque for maior que a contagem da lista
        if valorSaque >= lista[cont]:
            #Executar quantidade de notas
            notas = valorSaque // lista[cont]
            #Pega o resto da divisão
            valorSaque = valorSaque % lista[cont]
            print(f"Total de {notas} notas de R$ {lista[cont]} ")
            print(valorSaque)
        else:
            cont += 1
        if valorSaque == 0:
            break


if __name__ == "__main__":
    #validacao_dados()
    #jogo_adivinhacao_ver2()
    #menu_opcoes()
    #fatorial()
    #progressaoaritmetica_ver2()
    #progressaoaritmetica_ver3()
    #sequencia_fibonacci()
    #tratando_valores()
    #maior_menor_valores()
    #tratando_valores2()
    #tabuada_ver3()
    #par_impar()
    #analise_dados_grupo()
    #estatisticas_produtos()
    caixa_eletronico()




#pensar numa nova forma de fazer a tabuada
def tabuada():
    num = int(input("Digite um numero para conferir sua tabuada "))
    print("{} X {} = {}".format(num, 1, num*1))
    print("{} X {} = {}".format(num, 2, num * 2))
    print("{} X {} = {}".format(num, 3, num * 3))
    print("{} X {} = {}".format(num, 4, num * 4))
    print("{} X {} = {}".format(num, 5, num * 5))
    print("{} X {} = {}".format(num, 6, num * 6))
    print("{} X {} = {}".format(num, 7, num * 7))
    print("{} X {} = {}".format(num, 8, num * 8))
    print("{} X {} = {}".format(num, 9, num * 9))
    print("{} X {} = {}".format(num, 10, num * 10))

def conversor_de_moedas():
    d = float(input("Quanto de dinheiro você possui? R$ "))
    dolar = d / 5.53
    print("Com R${:.2f}, você pode comprar U${:.2f}".format(d, dolar))
    
def pintar_parede():
    width = float(input("Digite a largura da parede: "))
    height = float(input("Digite a altura da parede: "))
    area = height*width
    tinta = area/2
    print("Sua parede tem a dimensão de {}x{} e sua área é de {} m²".format(width, height, area))
    print("Para pintá-la você precisará {} litros".format(tinta))

def dar_desconto_ou_aumento():
    preco = float(input("Quanto custa o produto? R$ "))
    des = int(input("Qual o valor de desconto desse produto? "))
    aumento = True
    novopreco_menos = preco - (preco * des/100)
    novopreco_mais = preco + (preco * des/100)
    if aumento == True:
        pass
    print("O preço do produto é R${:.2f}, e com o desconto de {}%, o preço ficara R${}".format(preco, des, novopreco_menos))
    print("O preço do produto é R${:.2f}, e com o reajuste de {}%, o preço ficará R${}".format(preco, des, novopreco_mais))

def reajuste_salarial():
    salario = float(input("Qual é o seu salário? R$ "))
    por = int(input("Qual a porcentagem de reajuste? "))
    reajuste = salario + (salario * por/100)
    print("O seu salário é {}, e com o reajuste de {}%, você receberá R${:.2f}".format(salario, por, reajuste))

def conversor_de_temp():
    c = int(input("Qual a temperatura em Cº? "))
    f = (c * 1.8) + 32
    print("Se a temperatura em Cº é de {}, então a temperatura em Fahrenheit é: {}Fº".format(c, f))

def aluguel_de_carros():
    fixo = 500
    dia = int(input("Quantos dias foram alugados? ")) * 60
    kmrodados = int(input("Quantos km foram rodados? ")) * 0.15
    precofinal = fixo + dia + kmrodados
    print("O preço a se pagar é igual a {}".format(precofinal))

if __name__ == "__main__":
    #tabuada()
    #conversor_de_moedas()
    #pintar_parede()
    #dar_desconto_ou_aumento()
    #reajuste_salarial()
    #conversor_de_temp()
    aluguel_de_carros()
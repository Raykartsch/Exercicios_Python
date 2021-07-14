def conversor(value):
    value = "{:.2f}".format(float(value)* 9.537*10**-7)
    return value

def percentual(users, total):
    for i in range(len(users)):
        percent = "{:.2f}".format((float(users[i]['using_memory']) / total) * 100)
        users[i]['use_percentage'] = percent

def lerArquivo(archive):
    with open(archive, 'r') as readfile:
        total = 0
        users = []
        for linha in readfile:
            linha = linha.split()
            valor = conversor(linha[1])
            total += float(valor) 
            users.append({'nome': linha[0], 'using_memory': valor})      
        total = float(f"{total:.2f}")
        return total, users

def printarTabela(tabUsers, total):
    print()
    print("-"*50)
    print('Id'.ljust(5), 'User'.ljust(15), 'Using Space (MB)'.ljust(20), 'Use Percentage (%)')
    print("-"*50)
    for i in range(len(tabUsers)):
        print(str(i+1).ljust(5), 
        tabUsers[i]['nome'].ljust(15),
        tabUsers[i]['using_memory'].ljust(9) + 'MB'.ljust(11), 
        tabUsers[i]['use_percentage'] + '%')

    print("-"*50)
    print(f"O valor total utilizado pelos usuários: {total} MB")
    print(f"O valor médio de espaço utilizado: {total/len(tabUsers):.2f} MB")
    print("-"*50)
    


valor_convertido = lerArquivo('relatorio.txt')

total, users = lerArquivo('relatorio.txt')
percentual(users, total)
print(users)
printarTabela(users, total)



        


    




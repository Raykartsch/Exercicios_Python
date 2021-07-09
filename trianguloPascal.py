def trianguloPascal(num):
    matriz = []
    for i in range(0, num):
        matriz.append(1)
        matriz[i] = [1]
        for j in range(0, i):
            if i > 1 and j >= 1:
                for k in range(i-i+1, i):   
                    aux = matriz[i-1][j-1] + matriz[i-1][j]          
                    matriz[i][j] = aux
                print(matriz[i-1][j-1], '+', matriz[i-1][j])
                matriz[i].append(1)
            else:
                matriz[i].append(1)
            print(matriz[i])
            print('i: ',i, '- j: ',j)
            print('-'*50)
    return matriz

pascal = trianguloPascal(8)

for i in range(len(pascal)):
    print(pascal[i])
    print()

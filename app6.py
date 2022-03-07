import statistics
import math

caminho = str(input("bem-vindo à calculadora de modelos estatísticos, \ndigite o caminho do arquivo que deseja trabalhar: "))
arquivo = open(caminho,"r+")
conjunto = (arquivo.readlines())

for index in range(len(conjunto)):
    conjunto[index] = int(conjunto[index])

print(f"seu conjunto é: {conjunto}\n")

conjunto.sort()

print(f"seu conjunto ordenado é: {conjunto}\n")


def desvio_padrao():
    conjunto_diferenca = []
    for index in range(len(conjunto)):
        conjunto_diferenca.append(math.pow(conjunto[index]-statistics.mean(conjunto),2))
    somatoria = sum(conjunto_diferenca)
    desvio = math.sqrt(somatoria/len(conjunto))
    return desvio

def desvio_medio():
    conjunto_diferenca = []
    for index in range(len(conjunto)):
        conjunto_diferenca.append(abs(conjunto[index] - statistics.mean(conjunto)))
    somatoria = sum(conjunto_diferenca)
    desvio = somatoria/len(conjunto)
    return desvio

opcao = 0

while opcao != 1:
    print('''
    [1]terminar programa
    [2]média aritmética
    [3]média geométrica
    [4]desvio padrão
    [5]desvio médio
    [6]maior valor da sequência
    [7]menor valor da sequência
    [8]moda
    [9]mediana
    [10]variância
    [11]exibir o conjunto ordenado novamente

    ''')
    opcao = int(input("digite a opção desejada: "))
    if opcao == 2:
        print(f"sua média aritmética é: {statistics.mean(conjunto)}\n")
    elif opcao == 3:
        print(f"sua média geométrica é :{statistics.geometric_mean(conjunto)}\n")
    elif opcao == 4:
        print(f"seu desvio padrão é {desvio_padrao()}")
    elif opcao == 5:
        print(f"seu desvio médio é: {desvio_medio()}")
    elif opcao == 6:
        print(f"seu valor máximo é {max(conjunto)}")
    elif opcao == 7:
        print(f"seu valor mínimo é {min(conjunto)}")
    elif opcao == 8:
        print(f"a moda é {statistics.mode(conjunto)}")
    elif opcao == 9:
        print(f"a mediana é {statistics.median(conjunto)}")
    elif opcao == 10:
        print(f"a variância é {statistics.variance(conjunto)}")
    elif opcao == 11:
        print(f"seu conjunto ordenado é: {conjunto}")
    elif opcao > 11 or opcao < 1:
        print("opção inválida, digite uma opção válida")
    

    
print("fim do programa, obrigado por usar a calculadora de elementos estatísticos!")




arquivo.close()
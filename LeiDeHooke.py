from cmath import sqrt
import math
from xml.etree.ElementTree import tostring


# Funcoes

# Calcular o valor médio
def calculo_valorMedio (lista_x, n):

    soma_dos_x = 0
    for x in lista_x:
        soma_dos_x = soma_dos_x+x
    valor_medio = soma_dos_x/n

    print("Soma dos x: ",soma_dos_x)
    print("Valor médio: ",valor_medio)
    print("")
    return valor_medio

# Calcular Desvio Padrão da Medida - DPM
def calculo_dpm (lista_x, valor_medio):
    somatorio_dpm = 0
    for x in lista_x:
        valor_elemento = (x-valor_medio)**2
        somatorio_dpm = somatorio_dpm+valor_elemento

    divisao_dpm = somatorio_dpm/(n-1)
    raiz_dpm = (divisao_dpm)**(1/2)
    dpm = raiz_dpm

    print("Somatorio DPM: ",somatorio_dpm)
    print("Divisão DPM: ",divisao_dpm)
    print("Raiz DPM: ",raiz_dpm)
    print("DPM: ",dpm)
    print("")
    return dpm

#Calcular o sigmaA = DPM/raiz(n)
def calculo_sigmaA (dpm, n):
    sigmaA = dpm/(n**(1/2))

    print("SigmaA: ",sigmaA)
    print("")
    return sigmaA


# Calcular Incerteza Total: sigmaT
def calculo_sigmaT (sigmaA, sigmaB):
    print("Calculo da Incerteza Total: sigmaT")

    sigmaT = (sigmaA**2+sigmaB**2)**(1/2)

    print("Sigma T: ", sigmaT)
    print("")
    return sigmaT

# Calcular Volume do Cilindro
def calculo_VolumeMedio (dMedio, LMedio):
    volumeMedio = (math.pi * (dMedio**2) * LMedio)/4
    print("Volume Médio: ",volumeMedio)
    return volumeMedio



##################### Valores constantes:


# Valor da Incerteza Instrumental - sigmaB
sigmaB = 0.0005


# Valor da Massa:
massa = 0.01

# Quantidade de medidas
#n = int(input("Quantidade de medições (n): "))
n = 3

# Valores medidos de D:
lista_a = [0.260, 0.260, 0.260]

# Valores medidis de L:
#lista_l = [9.25,9.21,9.22,9.26,9.30,9.30,9.25,9.25,9.25,9.25]






##########################
# Funcionamento do Programa

print("\nSigmaB do Instrumento: ", sigmaB)
print("Valor da massa: ", massa)
print("Quantidade colhida: ",n)
print("Valores de A: ",lista_a)
#print("Valores de L: ",lista_l)
print("")



print("\n====\nAgora os outros Calculos\n")

valorMedio = calculo_valorMedio(lista_a, n)
print(valorMedio)






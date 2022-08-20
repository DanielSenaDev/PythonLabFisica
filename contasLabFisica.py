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



#####################
# Valores constantes:

## Valor da Incerteza Instrumental - sigmaB
# Menor graduação = 0,1 cm
#sigmaB = menorGraduação/2

sigmaB = 0.05

### Calcular sigmaB colocando os valores no console:
"""
graduacao_instrumento = float(input("Digite o valor da graduação do instrumento: "))
sigmaB = graduacao_instrumento/2
"""

## Valor da Massa:
massa = 284.1

## Quantidade de medidas
#n = int(input("Quantidade de medições (n): "))
n = 7

## Valores medidos de D:
#lista_d = [3.70,3.72,3.75,3.70,3.75,3.77,3.75,3.75,3.70,3.70]
#lista_d = [3.95, 3.80, 3.65]
lista_d = [6.95, 6.65, 6.20, 6.65, 6.60, 6.50, 6.70]

## Valores medidis de L:
#lista_l = [9.25,9.21,9.22,9.26,9.30,9.30,9.25,9.25,9.25,9.25]
#lista_l = [9.60, 9.40, 9.60]
lista_l = [20.90, 20.10, 20.85, 20.20, 19.25, 20.75, 18.55]

### Retirar as aspas caso os valores de x forem ser adicionados manualmente pelo console
"""
#Receber os valores de x pelo console
lista_x = []
ind_x=1
while(ind_x<=n):
    #print("Digite o Valor de x"+str(n))
    valor_de_x = float(input("Digite o Valor de x"+str(ind_x)+": "))
    lista_x.append(valor_de_x)
    ind_x = ind_x+1
"""




##########################
# Funcionamento do Programa

print("\nSigmaB do Instrumento: ", sigmaB)
print("Valor da massa: ", massa)
print("Quantidade colhida: ",n)
print("Valores de D: ",lista_d)
print("Valores de L: ",lista_l)
print("")


print("\n====\nCalculos do Diametro D\n")
dMedio = calculo_valorMedio(lista_d, n)
dpm_D = calculo_dpm(lista_d, dMedio)
sigmaA_D = calculo_sigmaA(dpm_D, n)
sigmaT_D = calculo_sigmaT(sigmaA_D, sigmaB)

print("\n====\nCalculos da Largura L\n")
lMedio = calculo_valorMedio(lista_l, n)
dpm_L = calculo_dpm(lista_l, lMedio)
sigmaA_L = calculo_sigmaA(dpm_L, n)
sigmaT_L = calculo_sigmaT(sigmaA_L, sigmaB)

print("\n====\nAgora os outros Calculos\n")

volumeMedio = calculo_VolumeMedio(dMedio, lMedio)





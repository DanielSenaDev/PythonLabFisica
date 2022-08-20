# Calcular o valor médio
import math


def calculo_valorMedio (lista_x):

    soma_dos_x = 0
    for x in lista_x:
        soma_dos_x = soma_dos_x+x
    valor_medio = soma_dos_x/len(lista_x)   
    return valor_medio

# Calcular Desvio Padrão da Medida - DPM
def calculo_dpm (lista_x, valor_medio):
    somatorio_dpm = 0
    for x in lista_x:
        valor_elemento = (x-valor_medio)**2
        somatorio_dpm = somatorio_dpm+valor_elemento

    divisao_dpm = somatorio_dpm/(len(lista_x)-1)
    raiz_dpm = (divisao_dpm)**(1/2)
    dpm = raiz_dpm
    '''
    print("Somatorio DPM: ",somatorio_dpm)
    print("Divisão DPM: ",divisao_dpm)
    print("Raiz DPM: ",raiz_dpm)
    print("DPM: ",dpm)
    print("")
    '''
    return dpm

# Calcular o sigmaA = DPM/raiz(n)
def calculo_sigmaA (dpm, n):
    sigmaA = dpm/(n**(1/2))

    #print("SigmaA: ",sigmaA)
    #print("")
    return sigmaA

# Calculo direto do sigma A dos valores das medições
def calculo_resultado_sigmaA (lista_x, n):
    valor_medio = calculo_valorMedio(lista_x)
    valor_dpm = calculo_dpm(lista_x, valor_medio)
    valor_sigmaA = calculo_sigmaA(valor_dpm, n)

    print("Valor médio: ",valor_medio)
    print("Sigma A: ", valor_sigmaA)

    return valor_sigmaA

# Calcular sigma C Combinado
def calculo_sigmaC(sigmaA, sigmaB):
    valor_sigmaC = (sigmaA**2+sigmaB**2)**(1/2)
    print("Sigma C: ", valor_sigmaC)
    return valor_sigmaC

# Calcular Periodo e SigmaA Periodo
def calculo_gravidade(valor_k, valor_distancia, tempo_medio):

    #valor_gravidade = 2 * math.pi * math.sqrt((valor_k+(valor_distancia**2))/(valor_distancia*gravidade))
    valor_periodo_T = 0 #criei variavel so para tirar erro do VSCode - n lembro para que serve essa fnção
    print(f"Valor Periodo T: {valor_periodo_T}")

    return valor_periodo_T

# Calculo do Periodo
def calculo_periodoT(tempo_medio, qtd_oscilacoes):
    periodo_T = tempo_medio/qtd_oscilacoes
    print(f"Valor do periodo T: {periodo_T}")
    return periodo_T

# Calculo da Incerteza do Periodo
def calculo_inc_periodoT(periodo_T, sigmaA_t, qtd_oscilacoes):
    inc_periodoT = sigmaA_t/qtd_oscilacoes
    print(f"Valor da Incerteza do periodo T: {inc_periodoT}")
    return inc_periodoT


##########
print("\n=====\nINICIO RESPOSTAS\n=====\n")
sigmaB_trena = 0.0005 #metros
sigmaB_tempo = 0.01 #segundos

#Quantidade de Oscilacoes
qtd_oscilacoes = 5

# Barra
barra_altura = 1.5000
barra_largura = 0.0100
b = barra_altura
a = barra_largura

valor_k = (a**2+b**2)/12 # m^2
print (f"\nValor de k(m^2): {valor_k}\n")

#Distancia do orifício até o centro de massa e as respectivas medidas de tempo
# d1, (medida1, medida2, medida3, medida4, medida5)

lista_de_tuplas = []
medida_n = 0

# Medidas - 01
medida_n += 1
distancia = 0.1500 # metros
lista_medidas_tempo = [6.94, 6.93, 6.91, 6.99, 6.92] # segundos
tupla_distancia_medidas = (distancia, lista_medidas_tempo) # (d, [medida1, medida2, medida3, medida4, medida5])
lista_de_tuplas.append(tupla_distancia_medidas) # adicionando a tupla em uma lista

'''
valormedio = calculo_valorMedio(lista_medidas_tempo)
print (f"Valor Médio MEDIDA {medida_n}: {valormedio}")

sigmaA = calculo_resultado_sigmaA(lista_medidas_tempo, 5)
print(f"Valor SigmaA MEDIDA {medida_n}: {sigmaA}")
'''

# Medidas - 02
medida_n += 1
distancia = 0.2000 # metros
lista_medidas_tempo = [6.33, 6.29, 6.31, 6.34, 6.31] # segundos
tupla_distancia_medidas = (distancia, lista_medidas_tempo) # (d, [medida1, medida2, medida3, medida4, medida5])
lista_de_tuplas.append(tupla_distancia_medidas) # adicionando a tupla em uma lista




# Medidas - 03
medida_n += 1
distancia = 0.3000 # metros
lista_medidas_tempo = [5.65, 5.70, 5.75, 5.71, 5.81] # segundos
tupla_distancia_medidas = (distancia, lista_medidas_tempo) # (d, [medida1, medida2, medida3, medida4, medida5])
lista_de_tuplas.append(tupla_distancia_medidas) # adicionando a tupla em uma lista




# Medidas - 04
medida_n += 1
distancia = 0.4000 # metros
lista_medidas_tempo = [5.46, 5.60, 5.47, 5.47, 5.56] # segundos
tupla_distancia_medidas = (distancia, lista_medidas_tempo) # (d, [medida1, medida2, medida3, medida4, medida5])
lista_de_tuplas.append(tupla_distancia_medidas) # adicionando a tupla em uma lista




# Medidas - 05
medida_n += 1
distancia = 0.6000 # metros
lista_medidas_tempo = [5.53, 5.57, 5.59, 5.58, 5.64] # segundos
tupla_distancia_medidas = (distancia, lista_medidas_tempo) # (d, [medida1, medida2, medida3, medida4, medida5])
lista_de_tuplas.append(tupla_distancia_medidas) # adicionando a tupla em uma lista

# Medidas - 06 (PROVA 2)
medida_n += 1
distancia = 0.6000 # metros
lista_medidas_tempo = [4.25, 4.59, 4.93] # segundos
tupla_distancia_medidas = (distancia, lista_medidas_tempo) # (d, [medida1, medida2, medida3, medida4, medida5])
lista_de_tuplas.append(tupla_distancia_medidas) # adicionando a tupla em uma lista
'''
# Medidas - 07 (PROVA 2- Anto)
medida_n += 1
distancia = 0.6000 # metros
lista_medidas_tempo = [4.18, 4.50, 5.00] # segundos
tupla_distancia_medidas = (distancia, lista_medidas_tempo) # (d, [medida1, medida2, medida3, medida4, medida5])
lista_de_tuplas.append(tupla_distancia_medidas) # adicionando a tupla em uma lista
'''




###
dicionario = dict([])
chave = 1
for el_tupla in lista_de_tuplas:
    dicionario.update({chave:el_tupla})
    chave = chave + 1 

chave = 1
for el in dicionario:
    print("\nMEDIDAS ", chave)
    tupla_in_dic = dicionario[chave]
    distancia_in_tupla = tupla_in_dic[0]
    lista_medidas_in_tupla = tupla_in_dic[1]

    #print_valores(massa_in_tupla, lista_medidas_in_tupla)

    valor_sigmaA = calculo_resultado_sigmaA(lista_medidas_in_tupla, len(lista_medidas_in_tupla))
    valor_sigmaC = calculo_sigmaC(valor_sigmaA, sigmaB_tempo)
    
    valor_Medio = calculo_valorMedio(lista_medidas_in_tupla)

    valor_periodo_T = calculo_periodoT(valor_Medio, qtd_oscilacoes)
    #valor_sigma_periodo_T = calculo_incerteza_periodoT()

    valor_inc_periodoT = calculo_inc_periodoT(valor_periodo_T, valor_sigmaA, qtd_oscilacoes)

    chave += 1


print("\n=====\nFIM RESPOSTAS\n=====\n")
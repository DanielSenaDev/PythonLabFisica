# Funcoes

# Printar valores que estão sendo trabalhados
def print_valores(massa,lista):
    print("Massa: ",massa," kg")
    print("Valores das medidas: ",lista," m")
    return 0

# Calcular o valor médio
def calculo_valorMedio (lista_x, n):

    soma_dos_x = 0
    for x in lista_x:
        soma_dos_x = soma_dos_x+x
    valor_medio = soma_dos_x/n    
    return valor_medio

# Calcular Desvio Padrão da Medida - DPM
def calculo_dpm (lista_x, valor_medio, n):
    somatorio_dpm = 0
    for x in lista_x:
        valor_elemento = (x-valor_medio)**2
        somatorio_dpm = somatorio_dpm+valor_elemento

    divisao_dpm = somatorio_dpm/(n-1)
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
    valor_medio = calculo_valorMedio(lista_x,n)
    valor_dpm = calculo_dpm(lista_x, valor_medio, n)
    valor_sigmaA = calculo_sigmaA(valor_dpm, n)

    print("Valor médio: ",valor_medio)
    print("Sigma A: ", valor_sigmaA)

    return valor_sigmaA

# Calcular sigma C Combinado
def calculo_sigmaC(sigmaA, sigmaB):
    valor_sigmaC = (sigmaA**2+sigmaB**2)**(1/2)
    print("Sigma C: ", valor_sigmaC)
    return valor_sigmaC

# Calcular Delta X
def calculo_deltax (x_inicial, x_final):
    deltax = x_final-x_inicial
    print("Delta X: ", deltax)
    return deltax

def calculo_sigma_deltax(x_inicial, x_final):
    valor_sigma_deltax = 0

    return valor_sigma_deltax



#############

print("\n#####\nInicio\n#####\n")
lista_tuplas = []


# ADICIONAR VALORES AQUI ABAIXO
#
#
#

#sigmaB - Instrumento
sigmaB = 0.0005
print("\nSIGMA B: ", sigmaB)

# X inicial
x_inicial = 0.251

# Medidas 1
massa = 0.01
lista_medidas = [0.260, 0.260, 0.260]
tupla_massa_medidas = (massa, lista_medidas)
lista_tuplas.append(tupla_massa_medidas)

# Medidas 2
massa = 0.03
lista_medidas = [0.275, 0.276, 0.276]
tupla_massa_medidas = (massa, lista_medidas)
lista_tuplas.append(tupla_massa_medidas)



#
# 
# FIM DA ADIÇÃO DOS VALORES
 



# PROGRAMA  
#
#

dicionario = dict([])
chave = 1
for el_tupla in lista_tuplas:
    dicionario.update({chave:el_tupla})
    chave = chave + 1 



chave = 1
for el in dicionario:
    print("\nMEDIDAS ", chave)
    tupla_in_dic = dicionario[chave]
    massa_in_tupla = tupla_in_dic[0]
    lista_medidas_in_tupla = tupla_in_dic[1]

    print_valores(massa_in_tupla, lista_medidas_in_tupla)

    valor_sigmaA = calculo_resultado_sigmaA(lista_medidas_in_tupla, len(lista_medidas_in_tupla))
    valor_sigmaC = calculo_sigmaC(valor_sigmaA, sigmaB)
    
    x_final = calculo_valorMedio(lista_medidas_in_tupla, len(lista_medidas_in_tupla))
    valor_delta_x = calculo_deltax(x_inicial, x_final)
    valor_sigma_deltax = calculo_sigma_deltax(x_inicial, x_final)

    chave = chave + 1


print("\n\nFIM DO PROGRAMA\n")
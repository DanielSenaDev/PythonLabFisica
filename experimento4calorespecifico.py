#Calcular o valor médio
from cmath import sqrt
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

# temp i sistema, temp f sistema, temp i metal, temp f metal, massa metal, massa agua, calor agua
def calculo_calor_especifico(delta_temp_sistema, delta_temp_metal, massa_metal, massa_agua, calor_agua):
    calor_metal = - (massa_agua*calor_agua*delta_temp_sistema) / (massa_metal*delta_temp_metal)
    return calor_metal


def calculo_inc_calor_metal(calor_metal, m_agua, m_metal, delta_t_sist, delta_t_metal, sigmaB_balanca, sigmaB_termometro):
    inc_calor_metal = sqrt(((sigmaB_balanca/m_agua)*calor_metal)**2+((sigmaB_balanca/m_metal)*calor_metal)**2+((sigmaB_termometro/delta_t_sist)*calor_metal)**2+((sigmaB_termometro/delta_t_metal)*calor_metal)**2)
    
    return inc_calor_metal

def calculo_erro(valor_medido, valor_real):
    valor_erro = abs(valor_real - valor_medido)/valor_real
    valor_erro = valor_erro * 100
    return valor_erro

#'''
sigmaB_balanca = 0.01
sigmaB_termometro = 0.01

temp_inicial_sistema = 50.50
temp_final_sistema = 48.78
delta_temp_sistema = temp_final_sistema - temp_inicial_sistema
print(f"delta temp sistema = {delta_temp_sistema}")

temp_inicial_metal = 28.40
temp_final_metal = 48.78
delta_temp_metal = temp_final_metal - temp_inicial_metal

m_metal = 71.00
m_agua = 230.50
calor_especifico_da_agua = 1
'''

sigmaB_balanca = 0.01
sigmaB_termometro = 0.01

temp_inicial_sistema = 49.6
temp_final_sistema = 48.07
delta_temp_sistema = temp_final_sistema - temp_inicial_sistema
print(f"delta temp sistema = {delta_temp_sistema}")

temp_inicial_metal = 27.84
temp_final_metal = 48.07
delta_temp_metal = temp_final_metal - temp_inicial_metal

m_metal = 69.00
m_agua = 231.00
calor_especifico_da_agua = 1
'''
#######

resultado_calor_especifico = calculo_calor_especifico(delta_temp_sistema, delta_temp_metal, m_metal, m_agua, calor_especifico_da_agua)

resultado_inc_cM = calculo_inc_calor_metal(resultado_calor_especifico, m_agua, m_metal, delta_temp_sistema, delta_temp_metal, sigmaB_balanca, sigmaB_termometro)

calor_real_aluminio = 0.22
resultado_erro = calculo_erro(resultado_calor_especifico, calor_real_aluminio)

print("\n---------\n")

print(f"Calor Especifico do Metal: {resultado_calor_especifico}")
print(f"Incerteza do Calor Especifico do Metal: {resultado_inc_cM}")
print(f"Erro Percentual Abosoluto relação ao calor específico do alumínio (cAL=0,22cal/g•°C): {resultado_erro} %")

print("\n---------\n")

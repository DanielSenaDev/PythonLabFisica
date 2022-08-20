import math


def calculo_volume_piramide_quad(l, h):
    volume_piramide = 1/3*(l**2)*h
    return volume_piramide

def calculo_area_superficei_cilindro(raio, l):
    valor_area_superficie = math.pi*raio*l
    return valor_area_superficie

"""
l = 3.53
h = 9.75

print("Volume: ")
print(calculo_volume_piramide_quad(l, h))
"""

raio = 6.6071428571428585
l = 20.085714285714285

print("\nCalculo areasuperficie")

area1 = calculo_area_superficei_cilindro(raio, l)
area2 = l*(raio*2)
area3 = math.pi*(raio**2)

area = area1+area2+area3

print(area)
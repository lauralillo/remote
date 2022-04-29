#prueba
import math

x = float(input('Escribe la coordenada X del punto: '))
y = float(input('Escribe la coordenada Y del punto: '))
m = float(input('Escribe la pendiente de la recta: '))
b = float(input('Escribe el término independiente de la recta: '))
d = abs((m * x - y + b)) / (math.sqrt(m ** 2 + 1))
print('La distancia del punto a la recta es: ',d)
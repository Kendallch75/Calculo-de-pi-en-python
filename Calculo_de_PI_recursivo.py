import random

# raíz cuadrada aproximada por bisección
def sqrt(n):
    i = 0
    s = n
    m = (i + s) / 2
    for _ in range(25):
        if m * m > n:
            s = m
        else:
            i = m
        m = (i + s) / 2
    return i

# distancia desde el origen
def distancia(tupla):
    x, y = tupla
    return sqrt(x*x + y*y)

# Metodo de simulacion para calcular pi
def Calculo_pi_simulacion(n):
    i = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if distancia((x, y)) <= 1:
            i += 1
    if i == 0:
        return 0 
    return 4 * (i / n)

# método de serie de Taylor para calcular pi
def Calculo_pi_series_de_Taylor(n):
    j = 0
    for i in range(n):
        if i & 1:
            j += -1 / (2*i + 1)
        else:
            j += 1 / (2*i + 1)
    return 4 * j

# main encargado de la impresion
def main():
    print("n se refiere a la cantidad de terminos en la serie de Taylor y pares ordenados utilizados en Simulacion")
    for i in range(17):
        n = 1 << i
        pi_prob = Calculo_pi_simulacion(n)
        pi_deter = Calculo_pi_series_de_Taylor(n)
        print(f"n = {n:<10} | Metodo de simulacion: {pi_prob:.10f} | Método series de Taylor: {pi_deter:.10f}")

main()

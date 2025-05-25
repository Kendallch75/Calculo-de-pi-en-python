import random

# raíz cuadrada por biseccion
def sqrt_aux(i, s, k):
    if k == 0:return i
    m = (i + s) / 2
    if m * m > s:return sqrt_aux(i, m, k - 1)
    else:return sqrt_aux(m, s, k - 1)

def sqrt(n):
    return sqrt_aux(0, n, 25)

# distancia desde el origen
def distancia(x, y):
    return sqrt(x*x + y*y)

# conteo recursivo
def contar_dentro(n, i=0, dentro=0):
    if i == n:return dentro
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if distancia(x, y) <= 1:return contar_dentro(n, i + 1, dentro + 1)
    else:return contar_dentro(n, i + 1, dentro)

# metodo simulacion
def Calculo_pi_simulacion(n):
    dentro = contar_dentro(n)
    if dentro == 0:return 0
    return 4 * (dentro / n)

# serie de Taylor 
def Calculo_pi_series_de_Taylor(n, i=0):
    if i == n:return 0
    if i&1:termino = -1/(2*i+1)
    else:termino= 1/(2*i+1)
    return termino + Calculo_pi_series_de_Taylor(n, i + 1)

# main recursivo
def main(i=0, max_i=9):
    if i == max_i:return
    n = 1 << i
    pi_prob = Calculo_pi_simulacion(n)
    pi_deter = 4 * Calculo_pi_series_de_Taylor(n)
    print(f"n = {n:<10} | Metodo de simulacion: {pi_prob:.10f} | Método series de Taylor: {pi_deter:.10f}")
    main(i + 1, max_i)

main()

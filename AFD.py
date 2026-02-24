import sys
import string

# Estados: q0, q1, q2, q3, q4, q5, q6
# Estados de Aceptación: q1, q2, q3, q4, q5
# q1 = SUMA
# q2 = INCR
# q3, q4, q5 = ID
# Estado de No Aceptación: q6

# Transiciones desde q0: q1, q3, q6
# Transiciones desde q1: q2, q6
# Transiciones desde q2: q6
# Transiciones desde q3: q3, q4, q5, q6
# Transiciones desde q4: q4, q5, q6
# Transiciones desde q5: q5, q4, q6

letrasM = list(string.ascii_uppercase)
letrasm = list(string.ascii_lowercase)
nums = list(string.digits)

def afd(entrada):
    q = 'q0'  # Estado inicial
    for n in entrada:
        if q == 'q0':
            if n in letrasM:
                q = 'q3'
            elif n == '+':
                q = 'q1'
            else:
                q = 'q6'
                break
        elif q == 'q1':
            if n == '+':
                q = 'q2'
            else:
                q = 'q6'
                break
        elif q == 'q3':
            if n in letrasM:
                q = 'q3'
            elif n in letrasm:
                q = 'q4'
            elif n in nums:
                q = 'q5'
            else:
                q = 'q6'
                break
        elif q == 'q4':
            if n in letrasm:
                q = 'q4'
            elif n in nums:
                q = 'q4'
            else:
                q = 'q6'
                break
        elif q == 'q5':
            if n in letrasm:
                q = 'q4'
            elif n in nums:
                q = 'q5'
            else:
                q = 'q6'
                break
        else:
            q = 'q6'
            break

try:
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        with open(entrada, 'r') as en:
            datos = en.read().split()
            for i in datos:
                afd(i)
    else:
        print("No se detectó archivo de entrada")

except:
    print("No se encontró el archivo")

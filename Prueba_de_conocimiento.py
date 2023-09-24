# EL SEGUNDO MAS GRANDE #1
# En una 'lista' de números, retorna el segundo número más grande.
#
# Ejemplo: [5,7,2,7,9,4,8]
# Respuesta: 8
numero = [5,7,2,7,9,4,8]
numero.sort() # con este metodo ordena los numero de manera desendente
print(numero[-2])

# CONVERSOR DE TIEMPO #2
# Crea una función que reciba días, horas, minutos y segundos 
# (como 'list') y retorne su resultado en milisegundos.
def Conversor(Dias=0, Horas =0, Minutos=0, Segundo=0):
    final_time=0
    Horas =+ Dias*24
    Minutos =+ Horas *60
    Segundo =+ Minutos * 60
    final_time =+ Segundo* 1000
    print(final_time)
Conversor(24,2,30,12)

# FIZZBUZZ #3
# Escribe una función que muestre por consola los números 
# de 1 a 100 (ambos incluidos y con un salto de línea entre
# cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
def FIZZBUZZ ():
    for a in range(1,101):
        if a % 3==0 and a % 5==0:
            print("fizzbuzz")
        elif a % 3==0:
             print("fizz")
        elif a % 5==0:
            print("buzz")
        else:
            print(a)
FIZZBUZZ()

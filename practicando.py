# hacer un programa que acepte dos numeros que imprima el mayor de los dos
# n1 = int(input("introdusca un numero"))
# n2 =int(input("introdusca un numero segundo numero"))

# if n1 > n2:
#     print(n1)
# elif n2 > n1:
#     print(n2)
# else:
#     print("no pueden ser iguales")
def funcion_max(n1:int, n2:int):

 if n1 > n2:
    return n1
 elif n2 > n1:
    return n2
 elif n1==n2:
   raise Exception("no pueden ser el mismo valor")
print(funcion_max(1,3))



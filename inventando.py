numero1 = int(input("Digite el primer numero"))
numero2= int(input("digite el segundo numero"))
operacion = str(input("eliga una opcion: 1)suma 2)Resta 3)Division 4)Multiplicacion"))
if operacion =="1":
    print(numero1+numero2)
elif operacion =="2":
    print(numero1-numero2)
elif operacion =="3":
    print(numero1 / numero2)
elif operacion=="4":
    print(numero1 * numero2)
else:
    print("no haz elegido una opcion correcta")


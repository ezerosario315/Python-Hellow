Numero1 = int(input("Introduzca un numero"))
Numero2 = int(input("Introduzca un numero"))
operaciones = str(input("elige un numero: 1.)Suma 2.)Resta 3.)Multipliacion 4.)Division "))

if operaciones == "1":
    print(Numero1+Numero2)
elif operaciones=="2":
    print(Numero1-Numero2)   
elif operaciones=="3":
    print(Numero1*Numero2)
elif operaciones=="4":
    print(Numero1/Numero2)
else:
    print("no haz elegido un numero correcto")
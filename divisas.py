#hacer un programa que me de la tasa de cambio de diferentes moneda.
#dollar =55.5
#Euro=61.05
Dinero_convetir= float(input("introduzca un monto"))
tasa_de_cambio = (input("eliga una moneda: P)Peso E)Euro D)Dollar." )).lower()#EL ERROE ERA QUE DEJE EL METODO ABIERTO 
#Y EL SISTEMA NO LO DETESTA COMO ERROR

if tasa_de_cambio =="p":
    peso = Dinero_convetir * 55.5
    print(peso)
elif tasa_de_cambio =="e":
    Euro =Dinero_convetir *61.01
    print(Euro)
elif tasa_de_cambio =="d":
    dollar=Dinero_convetir / 55.5
    print(dollar)
else:
    print("No haz elegido una moneda equivocada")
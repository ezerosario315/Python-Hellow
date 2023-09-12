#metodo viene siendo una función para ejercer diferente funciones.
Texto = "Hola Mundo"
print(Texto.upper())# metodo upper pasa todo el texto a mayuscula. el metodo es una función que viene incluida dentro de un objeto
print(Texto.lower())# todo minuscula
print(Texto.find("M"))#busca la posisicion del la letra en especifica
print(Texto.replace("Mun","Ezequiel Rosario"))
nuevoTExto=Texto.replace("Mun","Ezequiel Rosario")
print(Texto, nuevoTExto)
print("Mundo" in Texto)# es  una manera de buscar en el texto pero solo dara como verdadero o falso. un boolean

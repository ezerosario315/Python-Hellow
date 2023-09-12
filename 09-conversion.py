#progrma para hacer una convencion de temperatura
temperatura = float(input("ingrese una temperatura"))
escala = input("es Fahrenheit(F) o  Celsius(C): ").lower()

if escala == "f":
    celsius =(temperatura-32) * 5/9
    print(celsius)
elif escala =="c":
    fahrenheit = temperatura * 1.8 +32
    print(fahrenheit)
else:
    print("escala incorrecta")

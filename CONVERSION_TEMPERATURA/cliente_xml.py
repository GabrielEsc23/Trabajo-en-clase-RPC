import xmlrpc.client
cliente=xmlrpc.client.ServerProxy("http://localhost:8000/")

opcion=input("Ingresa la opción:\n"
    "1. Convertir de Celsius a Fahrenheit\n"
    "2. De Fahrenheit a Celsius\n"
    "Opción: ")

if opcion == "1":
    celsius = float(input("Ingresa la temperatura en Celsius: "))
    resultado = cliente.celsius_fahrenheit(celsius)
    print("Resultado en Fahrenheit:", resultado)

elif opcion == "2":
    fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
    resultado = cliente.fahrenheit_celsius(fahrenheit)
    print("Resultado en Celsius:", resultado)

else:
    print("Saliendo...")
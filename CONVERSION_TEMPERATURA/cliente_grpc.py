import grpc
import temperatura_pb2_grpc
import temperatura_pb2
cliente=grpc.insecure_channel(
    'localhost:5000'
)

#Crea el stub,llamar a la funciones remotas como:

stub=temperatura_pb2_grpc.ConvertirStub(
    cliente)

opcion=input("Ingresa la opción:\n"
    "1. Convertir de Celsius a Fahrenheit\n"
    "2. De Fahrenheit a Celsius\n"
    "Opción: "
    "3. Para salir ")

if opcion == "1":
    a=int(input("Ingresa el valor en grados celcius: "))

    r1=stub.CelciusFarenheit(temperatura_pb2.Parametros(valor=a))
    print(f"La temperatura en grados Farenhit es: {r1}")

elif opcion == "2":
    a=int(input("Ingresa el valor en grados farnheit: "))

    r2=stub.FarenheitCelcius(temperatura_pb2.Parametros(valor=a))
    print(f"La temperatura en grados Celcius es: {r2}")
    

else:
    print("Saliendo...")

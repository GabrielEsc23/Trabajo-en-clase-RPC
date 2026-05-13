import grpc
import calculadora_pb2_grpc,calculadora_pb2


#Crea un canal de comunicacion con el servidor
cliente=grpc.insecure_channel(
    'localhost:5000'
)
#Crea el stub,llamar a la funciones remotas como:

stub=calculadora_pb2_grpc.CalculadoraStub(
    cliente)

r1=stub.Sumar(
    calculadora_pb2.Operacion(a=10,b=5)
)
r2=stub.Restar(
    calculadora_pb2.Operacion(a=10,b=5)
)

r3=stub.Multiplicar(
    calculadora_pb2.Operacion(a=10,b=5)
)

r4=stub.Dividir(
    calculadora_pb2.Operacion(a=10,b=5)
)

print("La suma es: ", r1)
print("La la resta es: ", r2)
print("La multiplicación es: ", r3)
print("La dividir es: ", r4)


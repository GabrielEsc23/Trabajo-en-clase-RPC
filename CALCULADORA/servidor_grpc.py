import grpc
import calculadora_pb2_grpc,calculadora_pb2
from concurrent import futures



class CalculadoraServidor(
    calculadora_pb2_grpc.CalculadoraServicer):
    def Sumar(self,request,context):
        resultado= request.a + request.b 
        return calculadora_pb2.Resultado(
            resultado=resultado
        )
    def Restar (self,request,context):
        resultado= request.a - request.b 
        return calculadora_pb2.Resultado(
            resultado=resultado
        )
    def Multiplicar (self,request,context):
        resultado= request.a * request.b 
        return calculadora_pb2.Resultado(
            resultado=resultado
        )
    def Dividir (self,request,context):
        resultado= request.a /request.b 
        return calculadora_pb2.Resultado(
            resultado=resultado
        )
    
    
    
    
def serve():
        servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        calculadora_pb2_grpc.add_CalculadoraServicer_to_server(
            CalculadoraServidor(),
            servidor
        )

        servidor.add_insecure_port('[::]:5000')
        servidor.start()

        print("Servidor gRPC corriendo en el puerto 5000...")

        servidor.wait_for_termination()
        



serve()
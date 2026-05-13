import grpc
from concurrent import futures
import temperatura_pb2
import temperatura_pb2_grpc

class TemperaturaServidor(temperatura_pb2_grpc.ConvertirServicer):
    
    def CelciusFarenheit(self, request, context):
        resultado=(request.valor * 1.8) + 32
        return temperatura_pb2.Resultado(resultado=resultado)
    
    def FarenheitCelcius(self, request, context):
        resultado=(request.valor - 32) * 5/9
        return temperatura_pb2.Resultado(resultado=resultado)
    
    
    
def serve():
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    temperatura_pb2_grpc.add_ConvertirServicer_to_server(
        TemperaturaServidor(),
        servidor
    )

    servidor.add_insecure_port('[::]:5000')
    servidor.start()

    print("Servidor gRPC corriendo en el puerto 5000...")

    servidor.wait_for_termination()
serve()
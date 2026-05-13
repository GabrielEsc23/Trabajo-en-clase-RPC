from xmlrpc.server import SimpleXMLRPCServer

def celsius_fahrenheit(celsius):
    return (celsius * 1.8) + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


servidor = SimpleXMLRPCServer(("localhost", 8000))

servidor.register_function(celsius_fahrenheit, "celsius_fahrenheit")
servidor.register_function(fahrenheit_celsius, "fahrenheit_celsius")

print("Servidor XML-RPC corriendo en puerto 8000...")
servidor.serve_forever()

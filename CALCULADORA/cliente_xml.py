import xmlrpc.client

#Crear la conexión con el servidor
proxy=xmlrpc.client.ServerProxy("http://localhost:8000/")

a=int(input("Ingresa el primer número: "))
b=int(input("Ingresa el segundo número: "))

suma_resultado=proxy.sumar(a,b)
print(f"El resultado de la suma es: {suma_resultado}")

resta_resultado=proxy.restar(a,b)
print(f"El resultado de la resta es: {resta_resultado}")

multiplicacion_resultado=proxy.multiplicar(a,b)
print(f"El resultado de la multiplicación es: {multiplicacion_resultado}")

division_resultado=proxy.dividir(a,b)
print(f"El resultado de la división es: {division_resultado}")





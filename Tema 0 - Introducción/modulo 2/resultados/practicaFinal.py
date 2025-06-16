nombre = input("Ingrese su nombre: ")

ventas = float(input("Ingrese el monto de ventas del mes: "))

comision = ventas * 0.13

mensaje = f"Hola {nombre}, tu comisión este mes es de ${comision:.2f}."
print(mensaje)
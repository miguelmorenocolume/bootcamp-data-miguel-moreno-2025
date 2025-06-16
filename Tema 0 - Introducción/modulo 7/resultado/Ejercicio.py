class CuentaBancaria:
  def __init__(self, titular, saldo=0.0):
    self.titular = titular
    self.saldo = saldo

  # Método para ingresar dinero
  def ingresar(self, cantidad):
    if not self._es_cantidad_valida(cantidad):
      print("Cantidad no válida. Debe ser un número positivo.")
      return
    self.saldo += cantidad
    print(f"Ingreso realizado. Nuevo saldo: {self.saldo:.2f}€")

  # Método para retirar dinero
  def retirar(self, cantidad):
    if not self._es_cantidad_valida(cantidad):
      print("Cantidad no válida. Debe ser un número positivo.")
      return
    if cantidad > self.saldo:
      print("Saldo insuficiente para realizar la retirada.")
      return
    self.saldo -= cantidad
    print(f"Retirada realizada. Nuevo saldo: {self.saldo:.2f}€")

  # Método para consultar el saldo
  def consultar_saldo(self):
    print(f"Saldo actual: {self.saldo:.2f}€")

  # Método para transferir dinero a otra cuenta
  def transferir(self, cantidad, destinatario):
    comision = cantidad * 0.05
    total = cantidad + comision
    if not self._es_cantidad_valida(cantidad):
      print("Cantidad no válida. Debe ser un número positivo.")
      return
    if total > self.saldo:
      print("Saldo insuficiente para realizar la transferencia.")
      return
    self.saldo -= total
    destinatario.saldo += cantidad
    print(f"Transferencia realizada. Comisión: {comision:.2f}€. Nuevo saldo: {self.saldo:.2f}€")

  @staticmethod
  def _es_cantidad_valida(cantidad):
    return isinstance(cantidad, (int, float)) and cantidad > 0

# Clase derivada para cuentas premium
class CuentaPremium(CuentaBancaria):
  def __init__(self, titular, saldo=0.0):
    super().__init__(titular, saldo)
    self.telefono = None

  # Método para realizar una transferencia Bizum
  def bizum(self, cantidad, telefono_destino):
    if not self._es_cantidad_valida(cantidad):
      print("Cantidad no válida. Debe ser un número positivo.")
      return
    if cantidad > self.saldo:
      print("Saldo insuficiente para realizar la transferencia Bizum.")
      return
    self.saldo -= cantidad
    print(f"Bizum realizado a {telefono_destino}. Nuevo saldo: {self.saldo:.2f}€")

# Función para pedir una cantidad al usuario y manejar errores
def pedir_cantidad(mensaje):
  try:
    cantidad = float(input(mensaje))
    return cantidad
  except ValueError:
    print("Por favor, introduce un valor numérico válido.")
    return None

# Función principal para interactuar con el usuario
def main():
  print("====================CAJERO AUTOMÁTICO (Miguel Moreno Columé)====================")
  nombre = input("Introduce el nombre del titular de la cuenta: ")
  cuenta = CuentaPremium(nombre, saldo=0.0)

  while True:
    print("\n------------MENÚ PRINCIPAL-----------")
    print("1. Ingresar dinero")
    print("2. Retirar dinero")
    print("3. Consultar saldo")
    print("4. Transferencia bancaria (5% comisión)")
    print("5. Transferencia por Bizum (sin comisión)")
    print("6. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
      cantidad = pedir_cantidad("Cantidad a ingresar: ")
      if cantidad is not None:
        cuenta.ingresar(cantidad)
    elif opcion == "2":
      cantidad = pedir_cantidad("Cantidad a retirar: ")
      if cantidad is not None:
        cuenta.retirar(cantidad)
    elif opcion == "3":
      cuenta.consultar_saldo()
    elif opcion == "4":
      cantidad = pedir_cantidad("Cantidad a transferir: ")
      if cantidad is not None:
        destinatario = CuentaBancaria("Destinatario")
        cuenta.transferir(cantidad, destinatario)
    elif opcion == "5":
      if cuenta.telefono is None:
        telefono = input("Introduce tu número de teléfono para Bizum: ")
        if telefono.isdigit() and len(telefono) >= 9:
          cuenta.telefono = telefono
        else:
          print("Número de teléfono no válido.")
          continue
      cantidad = pedir_cantidad("Cantidad a transferir por Bizum: ")
      if cantidad is not None:
        telefono_destino = input("Introduce el número de teléfono del destinatario: ")
        if telefono_destino.isdigit() and len(telefono_destino) >= 9:
          cuenta.bizum(cantidad, telefono_destino)
        else:
          print("Número de teléfono del destinatario no válido.")
    elif opcion == "6":
      print("Gracias por utilizar el cajero. ¡Hasta pronto!")
      break
    else:
      print("Opción no válida.")

if __name__ == "__main__":
  main()
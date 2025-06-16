# Objetivo
Desarrollar una aplicación que funcione como un cajero automático interactivo, utilizando la consola para realizar las siguientes operaciones bancarias:

## Requisitos

### Operaciones Bancarias
- **Ingresar dinero**: Permitir al usuario añadir fondos a su cuenta.
- **Retirar dinero**: Permitir al usuario extraer dinero de su cuenta, asegurando que no se pueda retirar más del saldo disponible.
- **Consultar saldo**: Mostrar el saldo actual de la cuenta.
- **Transferencias bancarias**: Permitir la transferencia de dinero a otras cuentas, aplicando una comisión del 5% sobre el monto transferido.
- **Transferencias por Bizum**: 
  - Permitir al usuario realizar transferencias sin comisión a través de Bizum.
  - La primera vez que se use esta opción, se deberá pedir al usuario que introduzca su número de teléfono, el cual se almacenará para posteriores transferencias en esa sesión.
  - Además, cada vez que se utilice Bizum, deberá ingresarse el número de teléfono del destinatario (correspondiente a otra cuenta).

### Control de Errores
- Gestionar entradas no válidas por parte del usuario (como la introducción de valores negativos, montos no numéricos, opciones no válidas en el menú, etc.).
- Asegurarse de que las operaciones se realicen solo si hay suficiente saldo disponible.

## Flujo de la Aplicación
- El programa deberá estar estructurado en clases que representen las cuentas bancarias. Puedes definir una clase `CuentaBancaria` que cubra las operaciones básicas y extenderla para incluir transferencias y Bizum en una clase `CuentaPremium`.
- La aplicación debe estar organizada en un bucle continuo, mostrando el menú al usuario después de cada operación, hasta que el usuario decida salir.
- El número de teléfono del usuario para Bizum solo se pedirá la primera vez que se elija esa opción y no se solicitará de nuevo durante la sesión.

### Transferencias
- Las transferencias bancarias incluirán una comisión del 5% sobre el monto transferido.
- Las transferencias por Bizum no tendrán comisión, pero será necesario proporcionar el número del destinatario en cada operación.

### Interacción por Consola
- La interacción con el usuario se realizará completamente por consola. 
- Cada opción debe ser clara y proporcionar mensajes útiles tanto al realizar operaciones exitosas como al encontrarse con errores.

## Consejos Útiles
- Para llegar a la solución de este ejercicio deberás utilizar la POO (Programación Orientada a Objetos), explorarás las diversas soluciones que podemos aplicar gracias a esta a problemas tan cotidianos como manejar un cajero automatico.
- Si encuentras problemas a la hora de abordar este problema, te recomendamos revisar el Módulo 6. Y recuerda, ¡no tengas miedo a probar cosas e inclusive añadir funcionalidades, el límite es tu mente!

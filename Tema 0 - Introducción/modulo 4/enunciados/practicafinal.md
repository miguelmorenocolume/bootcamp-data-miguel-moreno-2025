### Juego Interactivo de Adivinanza de Números en Python

Escribe un programa en Python que implemente un juego interactivo de adivinanza de números siguiendo las reglas detalladas a continuación:

1. **Inicio del Juego:**
   - Solicita al usuario que ingrese su nombre.

2. **Generación del Número Secreto:**
   - El programa generará aleatoriamente un número secreto entre 1 y 100.

3. **Reglas del Juego:**
   - Informa al usuario que el programa ha pensado en un número y que tiene ocho intentos para adivinarlo.

4. **Proceso de Adivinanza:**
   - En cada intento, solicita al usuario que ingrese un número.
   - Valida el número ingresado y proporciona una respuesta según el caso:
     - Si el número está fuera del rango de 1 a 100, informa al usuario que ha elegido un número no permitido.
     - Si el número ingresado es menor que el número secreto, indica que el número elegido es menor al número secreto.
     - Si el número ingresado es mayor que el número secreto, indica que el número elegido es mayor al número secreto.
     - Si el usuario adivina correctamente el número secreto, felicita al usuario y muestra cuántos intentos le tomó adivinarlo.

5. **Terminación del Juego:**
   - Continúa solicitando números hasta que el usuario adivine el número secreto o se agoten los ocho intentos.
   - Una vez finalizados los intentos o al adivinar correctamente, muestra el número secreto si el usuario no lo adivinó.

**Recuerda:**
- Maneja correctamente los intentos y las respuestas del usuario para que el juego sea interactivo y amigable.
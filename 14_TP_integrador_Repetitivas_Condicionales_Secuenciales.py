# Ejercicio 1 - “Caja del Kiosco”
# 1. Nombre del cliente
while True:
    nombre = input("Ingrese su nombre: ")
    if nombre.isalpha() and nombre != "":
        break
    else:
        print("Error. Ingrese solo letras y no vacío")

# 2. Cantidad de productos
while True:
    cantidad = input("Ingrese la cantidad de productos a comprar: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error. Ingrese un numero entero positivo")

# Acumuladores
total_sin_descuento = 0
total_con_descuento = 0

# 3. Recorrer productos
for producto in range(1, cantidad + 1):

    # Precio
    while True:
        precio = input(f"Producto {producto} - Precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error. Ingrese un numero valido")

    # Descuento (S/N)
    while True:
        descuento = input("Descuento (S/N): ").lower()
        if descuento in ("s", "n"):
            break
        else:
            print("Error. Ingrese S o N")

    print(f"Producto {producto} - Precio: {precio} Descuento (S/N): {descuento}")

    # Acumular sin descuento
    total_sin_descuento += precio

    # Aplicar descuento
    if descuento == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio

    # Acumular con descuento
    total_con_descuento += precio_final

# 4. Resultados
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# Ejercicio 2 “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.

# Ejercicio 2 — Acceso al Campus

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    print(f"Intento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            while True:
                nueva = input("Nueva clave: ")

                if len(nueva) < 6:
                    print("Error: mínimo 6 caracteres.")
                    continue

                confirmacion = input("Confirmar clave: ")

                if nueva != confirmacion:
                    print("Error: no coinciden.")
                else:
                    clave_correcta = nueva
                    print("Clave cambiada correctamente.")
                    break

        elif opcion == 3:
            print("Seguí adelante, estás más cerca de lo que pensás.")

        elif opcion == 4:
            print("Saliendo...")
            break

# Ejercicio 3 — Agenda de Turnos (sin listas)

# Nombre operador
while True:
    operador = input("Ingrese nombre del operador: ")
    if operador.isalpha():
        break
    else:
        print("Error. Solo letras.")

# Turnos (vacíos = "")
lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

while True:
    print("\n1) Reservar 2) Cancelar 3) Ver día 4) Resumen 5) Salir")
    op = input("Opción: ")

    if not op.isdigit():
        print("Error")
        continue

    op = int(op)

    if op == 1:
        dia = input("1=Lunes 2=Martes: ")

        if dia == "1":
            while True:
                nombre = input("Paciente: ")
                if nombre.isalpha():
                    break

            if nombre in (lunes1, lunes2, lunes3, lunes4):
                print("Ya existe")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("Sin lugar")

        elif dia == "2":
            while True:
                nombre = input("Paciente: ")
                if nombre.isalpha():
                    break

            if nombre in (martes1, martes2, martes3):
                print("Ya existe")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("Sin lugar")

    elif op == 2:
        dia = input("1=Lunes 2=Martes: ")
        nombre = input("Nombre a cancelar: ")

        if dia == "1":
            if lunes1 == nombre: lunes1 = ""
            elif lunes2 == nombre: lunes2 = ""
            elif lunes3 == nombre: lunes3 = ""
            elif lunes4 == nombre: lunes4 = ""

        elif dia == "2":
            if martes1 == nombre: martes1 = ""
            elif martes2 == nombre: martes2 = ""
            elif martes3 == nombre: martes3 = ""

    elif op == 3:
        dia = input("1=Lunes 2=Martes: ")

        if dia == "1":
            print("Lunes:")
            print("1:", lunes1 if lunes1 else "(libre)")
            print("2:", lunes2 if lunes2 else "(libre)")
            print("3:", lunes3 if lunes3 else "(libre)")
            print("4:", lunes4 if lunes4 else "(libre)")

        elif dia == "2":
            print("Martes:")
            print("1:", martes1 if martes1 else "(libre)")
            print("2:", martes2 if martes2 else "(libre)")
            print("3:", martes3 if martes3 else "(libre)")

    elif op == 4:
        ocup_lunes = sum([lunes1!="", lunes2!="", lunes3!="", lunes4!=""])
        ocup_martes = sum([martes1!="", martes2!="", martes3!=""])

        print("Lunes:", ocup_lunes, "ocupados")
        print("Martes:", ocup_martes, "ocupados")

    elif op == 5:
        break

# Ejercicio 4 — Escape Room: La Bóveda

# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0  # para regla anti-spam

# Nombre del agente
while True:
    agente = input("Nombre del agente: ")
    if agente.isalpha():
        break
    else:
        print("Error: solo letras.")

# Bucle principal del juego
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("\n--- ESTADO ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras abiertas: {cerraduras_abiertas} | Alarma: {alarma}")
    print("1) Forzar cerradura  2) Hackear panel  3) Descansar")

    op = input("Opción: ")

    if not op.isdigit():
        print("Error: ingrese un número válido.")
        continue

    op = int(op)

    if op < 1 or op > 3:
        print("Error: opción fuera de rango.")
        continue

    # --- OPCIÓN 1: FORZAR ---
    if op == 1:
        racha_forzar += 1
        energia -= 20
        tiempo -= 2

        # Regla anti-spam (3 seguidas)
        if racha_forzar == 3:
            alarma = True
            print("La cerradura se trabó. ¡Alarma activada!")
            racha_forzar = 0
            continue

        # Riesgo de alarma si energía < 40
        if energia < 40:
            while True:
                riesgo = input("Riesgo (1-3): ")
                if riesgo.isdigit() and int(riesgo) in (1, 2, 3):
                    riesgo = int(riesgo)
                    break
                else:
                    print("Error: ingrese 1, 2 o 3.")

            if riesgo == 3:
                alarma = True
                print("¡Alarma activada!")
                continue

        # Si no hay alarma, abre cerradura
        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")

    # --- OPCIÓN 2: HACKEAR ---
    elif op == 2:
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        print("Hackeando...")
        for i in range(4):
            print(f"Paso {i+1}/4")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código suficiente! Se abrió una cerradura.")

    # --- OPCIÓN 3: DESCANSAR ---
    elif op == 3:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma te penaliza (-10 energía).")

    # Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado por alarma. DERROTA.")
        break

# Resultado final
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA. Te quedaste sin recursos.")

# Ejercicio 5 — La Arena del Gladiador

# Nombre del jugador
while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    else:
        print("Error: solo letras.")

# Estadísticas
hp_jugador = 100
hp_enemigo = 100
pociones = 3
juego_activo = True
turno_jugador = True

print("\n¡Comienza la batalla!")

while juego_activo:

    print(f"\n{nombre} HP: {hp_jugador} | Enemigo HP: {hp_enemigo}")

    if turno_jugador:
        print("1) Atacar  2) Curarse  3) Ataque crítico")

        op = input("Opción: ")

        if not op.isdigit():
            print("Error.")
            continue

        op = int(op)

        if op == 1:
            daño = 15
            hp_enemigo -= daño
            print(f"Atacaste por {daño}.")

        elif op == 2:
            if pociones > 0:
                hp_jugador += 20
                pociones -= 1
                print("Te curaste +20 HP.")
            else:
                print("No tenés pociones.")

        elif op == 3:
            daño = 15 * 1.5
            hp_enemigo -= int(daño)
            print(f"Golpe crítico por {int(daño)}.")

        else:
            print("Opción inválida.")
            continue

        turno_jugador = False

    else:
        print("El enemigo ataca...")
        hp_jugador -= 12
        turno_jugador = True

    # Condiciones de fin
    if hp_enemigo <= 0:
        print("¡GANASTE!")
        juego_activo = False
    elif hp_jugador <= 0:
        print("PERDISTE.")
        juego_activo = False
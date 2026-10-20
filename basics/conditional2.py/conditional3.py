

temperature = input("introduce the current temperature")

humidity = 0.2 


# Idea general: crear un programa que toma decisiones de riego 
# dependiendo de los factores de temperatura y humedad 
if humidity > 50: 
    print("irrigate 1L per square meter")  






# Programa sencillo de riego automatico

print("=== SISTEMA DE RIEGO ===")

# Introducimos los valores
temperatura = float(input("Introduce la temperatura actual en grados: "))
humedad = float(input("Introduce la humedad del suelo (0-100%): "))

print("\n--- RESULTADOS ---")
print("Temperatura:", temperatura, "grados")
print("Humedad del suelo:", humedad, "%")

# Tomamos decisiones segun la temperatura y la humedad

if humedad < 30:
    print("El suelo esta muy seco.")
    print("Hay que regar 1 litro de agua por metro cuadrado.")

elif humedad < 50 and temperatura > 25:
    print("El suelo tiene poca humedad y hace calor.")
    print("Hay que regar 0.5 litros de agua por metro cuadrado.")

elif humedad >= 50 and temperatura > 35:
    print("Hay bastante humedad, pero hace mucho calor.")
    print("Comprueba el suelo antes de regar.")

else:
    print("La humedad es suficiente.")
    print("No hace falta regar por ahora.")

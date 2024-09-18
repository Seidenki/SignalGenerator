import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# Parámetros
voltaje_bajo = 0.0
voltaje_alto = 5.0
rise_time = 1e-6  # 1 microsegundo
fall_time = 1e-6  # 1 microsegundo
frecuencia = 1e3  # 2 kHz
n_periodos = 100  # Número de periodos a graficar
ancho_pulso_inicial = 0.05  # 10% del periodo

# Calcula el periodo y el tiempo total
periodo = 1 / frecuencia
tiempo_total = n_periodos * periodo
n_puntos = 1000 * n_periodos
tiempo = np.linspace(0, tiempo_total, n_puntos)

# Inicializa el pulso
pulso = np.zeros(n_puntos)

# Define el tiempo de subida/bajada en índices
rise_samples = int(rise_time * n_puntos / tiempo_total)
fall_samples = int(fall_time * n_puntos / tiempo_total)

# Genera el pulso para cada periodo
for j in range(n_periodos):
    inicio_periodo = j * int(n_puntos / n_periodos)
    fin_periodo = (j + 1) * int(n_puntos / n_periodos)
    ancho_pulso = ancho_pulso_inicial + (j // 5) * 0.05
    
    for i in range(inicio_periodo, fin_periodo):
        t = tiempo[i] - j * periodo
        if t < rise_time:
            pulso[i] = voltaje_bajo + (voltaje_alto - voltaje_bajo) * (t / rise_time)
        elif t < (rise_time + (periodo * ancho_pulso)):
            pulso[i] = voltaje_alto
        elif t < (rise_time + (periodo * ancho_pulso) + fall_time):
            pulso[i] = voltaje_alto - (voltaje_alto - voltaje_bajo) * ((t - (rise_time + (periodo * ancho_pulso))) / fall_time)
        else:
            pulso[i] = voltaje_bajo

# Muestra el pulso
plt.figure(figsize=(12, 6))
plt.plot(tiempo, pulso, label='Pulso')
plt.title('Generador de Pulsos - 100 Periodos')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.grid(True)
plt.legend()
plt.show()

ruta_archivo = 'C:/Users/crisb/OneDrive/Documentos/Python Scripts/pulso.csv'

# Guardar en CSV
data = {'Tiempo (s)': tiempo, 'Voltaje (V)': pulso}
df = pd.DataFrame(data)
df.to_csv(ruta_archivo, index=False)
# Guardar en archivo de texto
with open(ruta_archivo, 'w') as archivo:
    for t, p in zip(tiempo, pulso):
        archivo.write(f"{t:.6f} {p:.6f}\n")

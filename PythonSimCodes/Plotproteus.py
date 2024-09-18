import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Lee el archivo CSV
df = pd.read_csv('CrescentPWM.csv')



# Crea una figura y un conjunto de subgráficas
plt.figure(figsize=(12, 6))

# Grafica cada columna
plt.plot(df['TIME'], df['PWM'], label='PWM', color='blue')
plt.plot(df['TIME'], df['Expected Output'], label='Out', color='red')

# Añade etiquetas y leyenda
plt.xlabel('Time')
plt.ylabel('Volts')

#plt.xticks( np.arange(0, 0.03, 0.002)  )
#plt.yticks( np.arange(0, 5.2, 0.2)  )
plt.title('PWM input and Analog Output vs Time')

plt.legend()

# Muestra la gráfica
plt.grid(True)
plt.show()

import random
import time

# Função que simula a leitura de um sensor de temperatura
def simular_temperatura():
    # Temperatura simulada entre 18°C e 30°C
    temperatura = random.uniform(18.0, 30.0)
    return round(temperatura, 2)

# Exibindo a temperatura a cada 2 segundos
while True:
    temperatura = simular_temperatura()
    print(f"Temperatura simulada: {temperatura}°C")
    time.sleep(2)  # Pausa de 2 segundos entre as leituras

import csv
import os
from random import choice
from datetime import datetime, timedelta

# Defina as datas para as quais você deseja gerar arquivos
dates = [datetime(2023, 5, 13), datetime(2023, 5, 14), datetime(2023, 5, 15)]

# Defina alguns exemplos de nomes de times e esportes
times = ['Time1', 'Time2', 'Time3', 'Time4', 'Time5']
esportes = ['Futebol', 'Basquete', 'Volei', 'Handball', 'Natacao']

# Caminho para a pasta onde os arquivos serão salvos
directory = './Data' 
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(20):  # Gerar 20 arquivos
    date = choice(dates)  # Escolher uma data aleatória das fornecidas
    filename = f'{date.strftime("%Y-%m-%d %H:%M:%S")}.csv'  # Criar o nome do arquivo com a data
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['nome_time', 'nome_esporte'])  # Escrever os cabeçalhos das colunas
        for _ in range(2):  # Cada arquivo terá 10 linhas de dados
            writer.writerow([choice(times), choice(esportes)])  # Escrever uma linha de dados

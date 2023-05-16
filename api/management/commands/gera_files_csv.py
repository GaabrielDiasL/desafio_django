import csv
import os
from random import choice
from datetime import datetime, timedelta


dates = [datetime(2023, 5, 13), datetime(2023, 5, 14), datetime(2023, 5, 15)]


times = ['Time1', 'Time2', 'Time3', 'Time4', 'Time5']
esportes = ['Futebol', 'Basquete', 'Volei', 'Handball', 'Natacao']

directory = './Data' 
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(20):  
    date = choice(dates)  
    filename = f'{date.strftime("%Y-%m-%d %H:%M:%S")}.csv' 
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['nome_time', 'nome_esporte'])  
        for _ in range(2):  
            writer.writerow([choice(times), choice(esportes)])  

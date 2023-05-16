from django.core.management.base import BaseCommand
import pandas as pd
import os
from api.models import Time, Esporte  # Importe os modelos
from django.db import transaction
from datetime import datetime, timedelta

class Command(BaseCommand):
    print("Iniciando importação dos arquivos")
    help = 'Importa arquivos .csv da pasta "Data" para o banco de dados'

    def handle(self, *args, **options):
        directory = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Data')
        yesterday = datetime.now() - timedelta(days=1)
        yesterday_date = yesterday.strftime('%Y-%m-%d')

        for filename in os.listdir(directory):
            if filename.endswith('.csv') and filename.startswith(yesterday_date):
                file_path = os.path.join(directory, filename)
                data = pd.read_csv(file_path)
                with transaction.atomic():
                    for index, row in data.iterrows():
                        esporte, _ = Esporte.objects.get_or_create(nome_esporte=row['nome_esporte'])
                        _, created = Time.objects.get_or_create(
                            nome_time=row['nome_time'],
                            nome_esporte=esporte,
                        )

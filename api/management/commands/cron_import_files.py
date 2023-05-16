from django.core.management.base import BaseCommand
from crontab import CronTab
import os

class Command(BaseCommand):
    help = 'Configura a tarefa cron para importar arquivos .csv diariamente'

    def handle(self, *args, **options):
        with CronTab(user='gabrieldias') as cron:
            manage_py_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'manage.py')
            job = cron.new(command=f'python {manage_py_path} import_files')
            job.setall('0 0 * * *')  # todos os dias às 00:00
            cron.write()

import os
from django.core.management.base import BaseCommand
from django.db import transaction
from food.models import IBGEFood
import csv


class Command(BaseCommand):
    help = 'Carrega dados nutricionais da tabela IBGE para o banco de dados'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            help='Caminho do arquivo CSV com os dados',
            default=os.path.join(os.path.dirname(__file__), 'data', 'ibge_data.csv')
        )

    @transaction.atomic
    def handle(self, *args, **options):

        def adjust_values(key, value):
            """Converte valores nutricionais para float, mantendo textos intactos"""

            if key in ('codigo', 'descricao_do_alimento',
                       'categoria', 'codigo_de_preparacao', 'descricao_da_preparacao'):
                return value
            else:
                return float(value)

        file_path = options['file']

        try:
            with open(file_path, 'r', encoding='latin1') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=';')

                total_created = 0
                for row in reader:
                    cleaned_data = {
                        key: None if value in ('', '-') else adjust_values(key, value)
                        for key, value in row.items()
                    }
                    IBGEFood.objects.create(**cleaned_data)
                    total_created += 1

                self.stdout.write(
                    self.style.SUCCESS(f'{total_created} registros criados com sucesso!')
                )

        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR('Arquivo não encontrado. Verifique o caminho: ' + file_path)
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Erro durante a importação: {str(e)}')
            )

import csv
from django.core.management.base import BaseCommand
from students.models import Student

class Command(BaseCommand):
    help = 'Load student data from CSV file'

    def handle(self, *args, **kwargs):
        with open('../student-dataset.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Student.objects.create(
                    id_no = row['id_no'],
                    name=row['name'],
                    nationality=row['nationality'],
                    city=row['city'],
                    gender=row['gender'],
                    age=row['age']
                )

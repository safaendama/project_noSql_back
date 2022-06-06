import csv
from .models import Phones


def load():
    path='./phones_app/phone_avito.csv'
    with open(path, encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        Phones.objects.all().delete()
        for row in reader:
            print(row)
            phone = Phones(City=row[2],Date=row[3],Brand=row[4],Model=row[5],Storage=row[6],Stat=row[7],Price=row[1])
            phone.save()

#load()
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'second_project.settings')

import django
django.setup()

from second_app.models import User
from faker import Faker
from faker.providers import person
from faker.providers import internet

fakegen = Faker()
fakegen.add_provider(person)
fakegen.add_provider(internet)

def populate(N=5):
    for entry in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        user = User.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)[0]

if __name__ == '__main__':
    print("populateing script!")
    populate(20)
    print("populating complete!")

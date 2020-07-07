import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','frst_project.settings')
import django
django.setup()
import random
from mysecApp.models import User
from faker import Faker

fake_gen = Faker()

# def add_topic():
#     t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
#     t.save()
#     return t

def populate(n=5):
    for _ in range(n):
        # top = add_topic()
        #create fake data for that entry
        fake_fname = fake_gen.first_name()
        fake_lname = fake_gen.last_name()
        fake_email = fake_gen.email()
        #create fake data for webpage entry
        usr = User.objects.get_or_create(first_name = fake_fname,last_name= fake_lname,email = fake_email)


if __name__ == "__main__":
    print("Populating Scripts ...")
    populate(20)
    print("Population Complete !")
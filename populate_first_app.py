import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','frst_project.settings')
import django
django.setup()
import random
from myApp.models import Topic,AccessRecord,Webpage
from faker import Faker

fake_gen = Faker()

topics = ['News','Marketplace','Games','Social']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for _ in range(n):
        top = add_topic()
        #create fake data for that entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()
        #create fake data for webpage entry
        wbpage = Webpage.objects.get_or_create(topic = top,url= fake_url,name = fake_name)[0]
        #create fake data for AccessRe entry
        acc_rec = AccessRecord.objects.get_or_create(name = wbpage,date = fake_date)[0]
        

if __name__ == "__main__":
    print("Populating Scripts ...")
    populate(20)
    print("Population Complete !")
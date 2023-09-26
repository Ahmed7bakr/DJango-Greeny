import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()

from products.models import Product,Category,Brand

import random
from faker import Faker

def seed_category(n):
    fake = Faker()
    images = ['1.png','2.png','3.png','4.png','5.png']
    

def seed_brand(n):
    pass

def seed_products(n):
    pass



seed_brand(10)
seed_category(10)
seed_products(50)
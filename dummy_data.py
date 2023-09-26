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
    
    for _ in range(n):

        name = fake.name()
        image = f"categorys/{images[random.randint(0,4)]}"

        Category.objects.create(
            name = name,
            image = image

        )
    
    print(f"successfully seeded {n} categorys")



def seed_brand(n):
    fake = Faker()
    images = ['1.png','2.png','3.png','4.png','5.png']
    
    for _ in range(n):

        name = fake.name()
        image = f"brands/{images[random.randint(0,4)]}"

        Brand.objects.create(
            name = name,
            image = image,
            category = Category.objects.get(id = random.randint(4,13))

        )

    print(f"successfully seeded {n} brands")




def seed_products(n):
    fake = Faker()
    images = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png']
    flag_type = ['New','Feature','Sale']
    for _ in range(n):

        name = fake.name()
        subtitle = fake.text(max_nb_chars=500)
        sku = random.randint(1000,100000)
        description = fake.text(max_nb_chars=10000)
        price = round(random.uniform(20.99,99.99),2)
        image = f"products/{images[random.randint(0,7)]}"
        flag = flag_type[random.randint(0,2)]
        quantity = random.randint(1,100)


        Product.objects.create(
            name = name,
            image = image,
            subtitle=subtitle,
            sku = sku,
            desc = description,
            price = price,
            flag = flag,
            quantity =quantity,
            brand = Brand.objects.get(id = random.randint(4,13)),
            category = Category.objects.get(id = random.randint(4,13))

        )

    print(f"successfully seeded {n} products")



seed_brand(10)
seed_category(10)
seed_products(1000)
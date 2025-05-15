import pandas as pd
from django.core.management.base import BaseCommand
from recommender.models import Products

class Command(BaseCommand):
    help = 'Load products from CSV file into the database'

    def handle(self, *args, **kwargs):
        csv_file = 'data/products.csv'
        df = pd.read_csv(csv_file)
        
        # Clear existing products
        Products.objects.all().delete()
        
        # Load products
        for _, row in df.iterrows():
            Products.objects.create(
                Product_id=row['product_id'],
                product_name=row['product_name'],
                category=row['category'],
                price=row['price'],
                description=row['description'],
                rating=row['rating'],
                image_url=row['image_url']
            )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {len(df)} products'))
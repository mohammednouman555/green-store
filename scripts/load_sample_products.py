# Run: python manage.py shell < scripts/load_sample_products.py
from store.models import Product
p1 = Product.objects.create(name='Ficus Indoor Plant', category='Plants', price=499.00, stock=20, description='Easy-care indoor plant.')
p2 = Product.objects.create(name='Rose Seeds', category='Seeds', price=99.00, stock=100, description='High germination rose seeds.')
p3 = Product.objects.create(name='Organic Fertilizer 1kg', category='Fertilizers', price=199.00, stock=50, description='NPK 5-5-5 organic fertilizer.')
p4 = Product.objects.create(name='Garden Shovel', category='Tools', price=349.00, stock=30, description='Sturdy garden shovel.')
print('Sample products created.')

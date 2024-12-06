from django.core.management.base import BaseCommand
from myapp.models import Toy  # Import your Toy model

class Command(BaseCommand):
    help = 'Create sample toys in the database'

    def handle(self, *args, **kwargs):
        # Create toys in the database
        Toy.objects.create(name="Toy Car", toy_type="Vehicle", price=9.99, stock=50)
        Toy.objects.create(name="Doll", toy_type="Figure", price=14.99, stock=30)

        self.stdout.write(self.style.SUCCESS('Successfully created Toy objects!'))
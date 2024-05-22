import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from django.contrib.auth import get_user_model
from products.models import Deposit, Saving, Annuity

User = get_user_model()

class Command(BaseCommand):
    help = 'Create dummy users and add them to products'

    def handle(self, *args, **kwargs):
        self.create_dummy_users(300)
        self.add_random_users_to_products()
        self.stdout.write(self.style.SUCCESS('Successfully created dummy data.'))

    def create_dummy_users(self, num_users):
        seeder = Seed.seeder()
        seeder.add_entity(User, num_users, {
            'username': lambda x: seeder.faker.email(),
            'password': lambda x: seeder.faker.password(),
            'nickname': lambda x: seeder.faker.user_name(),
            'age': lambda x: random.randint(18, 80),
            'gender': lambda x: random.choice(['M', 'F']),
            'asset': lambda x: random.randint(1000, 100000),
            'is_pension': lambda x: seeder.faker.boolean(),
            'is_internet': lambda x: seeder.faker.boolean(),
            'is_BLSR': lambda x: seeder.faker.boolean(),
            'is_free': lambda x: seeder.faker.boolean(),
        })
        seeder.execute()

    def add_random_users_to_products(self):
        all_users = list(User.objects.all())
        all_deposits = list(Deposit.objects.all())
        all_savings = list(Saving.objects.all())
        all_annuities = list(Annuity.objects.all())

        num_users_to_add = lambda: random.randint(100, 150)

        # For deposits
        for deposit in all_deposits:
            random_users = random.sample(all_users, k=num_users_to_add())
            deposit.deposit_joined_users.add(*random_users)

        # For savings
        for saving in all_savings:
            random_users = random.sample(all_users, k=num_users_to_add())
            saving.saving_joined_users.add(*random_users)

        # For annuities
        for annuity in all_annuities:
            random_users = random.sample(all_users, k=num_users_to_add())
            annuity.annuity_joined_users.add(*random_users)

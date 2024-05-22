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
            'asset': lambda x: random.randint(1000000, 1000000000),  # 100만원 ~ 10억원 사이의 랜덤값 설정
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

        for user in all_users:
            user_age = user.age
            user_is_internet = user.is_internet
            user_is_free = user.is_free

            # For deposits
            for deposit in all_deposits:
                age_filter = deposit.age_filter
                internet_filter = deposit.internet_filter
                gender_filter = deposit.gender_filter

                if age_filter == 0 or ((age_filter < 0 and user_age <= abs(age_filter)) or (age_filter > 0 and user_age >= age_filter)):
                    if (internet_filter and user_is_internet) or not user_is_internet:
                        if (user_is_free and not gender_filter) or not user_is_free:
                            deposit.deposit_joined_users.add(user)
                            deposit.deposit_like_users.add(user)

            # For savings
            for saving in all_savings:
                age_filter = saving.age_filter
                internet_filter = saving.internet_filter
                gender_filter = saving.gender_filter

                if age_filter == 0 or ((age_filter < 0 and user_age <= abs(age_filter)) or (age_filter > 0 and user_age >= age_filter)):
                    if (internet_filter and user_is_internet) or not user_is_internet:
                        if (user_is_free and not gender_filter) or not user_is_free:
                            saving.saving_joined_users.add(user)
                            saving.saving_like_users.add(user)

            # For annuities
            for annuity in all_annuities:
                age_filter = annuity.age_filter
                internet_filter = annuity.internet_filter
                gender_filter = annuity.gender_filter

                if age_filter == 0 or ((age_filter < 0 and user_age <= abs(age_filter)) or (age_filter > 0 and user_age >= age_filter)):
                    if (internet_filter and user_is_internet) or not internet_filter:
                        if (user_is_free and not gender_filter) or not user_is_free:
                            annuity.annuity_joined_users.add(user)
                            annuity.annuity_like_users.add(user)
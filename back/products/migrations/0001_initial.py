# Generated by Django 4.2.8 on 2024-05-20 22:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Saving",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dcls_month", models.TextField()),
                ("fin_co_no", models.TextField()),
                ("fin_prdt_cd", models.TextField()),
                ("kor_co_nm", models.TextField()),
                ("fin_prdt_nm", models.TextField()),
                ("join_deny", models.TextField(null=True)),
                ("join_member", models.TextField(null=True)),
                ("mtrt_int", models.TextField(null=True)),
                ("max_limit", models.TextField(null=True)),
                ("join_way", models.TextField(null=True)),
                ("spcl_cnd", models.TextField(null=True)),
                ("month_6", models.FloatField(null=True)),
                ("month_12", models.FloatField(null=True)),
                ("month_24", models.FloatField(null=True)),
                ("month_36", models.FloatField(null=True)),
                (
                    "saving_joined_users",
                    models.ManyToManyField(
                        related_name="saving_join_products", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "saving_like_users",
                    models.ManyToManyField(
                        related_name="saving_like_products", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Deposit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dcls_month", models.TextField()),
                ("fin_co_no", models.TextField()),
                ("fin_prdt_cd", models.TextField()),
                ("kor_co_nm", models.TextField()),
                ("fin_prdt_nm", models.TextField()),
                ("join_deny", models.TextField(null=True)),
                ("join_member", models.TextField(null=True)),
                ("mtrt_int", models.TextField(null=True)),
                ("max_limit", models.TextField(null=True)),
                ("join_way", models.TextField(null=True)),
                ("spcl_cnd", models.TextField(null=True)),
                ("month_6", models.FloatField(null=True)),
                ("month_12", models.FloatField(null=True)),
                ("month_24", models.FloatField(null=True)),
                ("month_36", models.FloatField(null=True)),
                (
                    "deposit_joined_users",
                    models.ManyToManyField(
                        related_name="deposit_join_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "deposit_like_users",
                    models.ManyToManyField(
                        related_name="deposit_like_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Annuity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dcls_month", models.TextField()),
                ("fin_co_no", models.TextField()),
                ("fin_prdt_cd", models.TextField()),
                ("kor_co_nm", models.TextField()),
                ("fin_prdt_nm", models.TextField()),
                ("join_deny", models.TextField(null=True)),
                ("join_member", models.TextField(null=True)),
                ("join_way", models.TextField(null=True)),
                ("pnsn_kind_nm", models.TextField(null=True)),
                ("prdt_type_nm", models.TextField(null=True)),
                ("avg_prft_rate", models.FloatField(null=True)),
                ("btrm_prft_rate_1", models.FloatField(null=True)),
                ("btrm_prft_rate_2", models.FloatField(null=True)),
                ("btrm_prft_rate_3", models.FloatField(null=True)),
                (
                    "annuity_joined_users",
                    models.ManyToManyField(
                        related_name="annuity_join_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "annuity_like_users",
                    models.ManyToManyField(
                        related_name="annuity_like_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
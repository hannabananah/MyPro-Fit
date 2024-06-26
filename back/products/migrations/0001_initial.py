# Generated by Django 4.2.8 on 2024-05-23 11:29

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
                ("join_deny", models.TextField(blank=True, null=True)),
                ("join_member", models.TextField(blank=True, null=True)),
                ("mtrt_int", models.TextField(blank=True, null=True)),
                ("max_limit", models.TextField(blank=True, null=True)),
                ("join_way", models.TextField(blank=True, null=True)),
                ("spcl_cnd", models.TextField(blank=True, null=True)),
                ("month_6", models.FloatField(blank=True, null=True)),
                ("month_12", models.FloatField(blank=True, null=True)),
                ("month_24", models.FloatField(blank=True, null=True)),
                ("month_36", models.FloatField(blank=True, null=True)),
                ("age_filter", models.IntegerField(blank=True, default=0, null=True)),
                ("gender_filter", models.TextField(blank=True, default="", null=True)),
                ("BLSR_filter", models.TextField(blank=True, default="", null=True)),
                ("internet_filter", models.BooleanField(blank=True, null=True)),
                (
                    "saving_joined_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="saving_join_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "saving_like_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="saving_like_products",
                        to=settings.AUTH_USER_MODEL,
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
                ("join_deny", models.TextField(blank=True, null=True)),
                ("join_member", models.TextField(blank=True, null=True)),
                ("mtrt_int", models.TextField(blank=True, null=True)),
                ("max_limit", models.TextField(blank=True, null=True)),
                ("join_way", models.TextField(blank=True, null=True)),
                ("spcl_cnd", models.TextField(blank=True, null=True)),
                ("month_6", models.FloatField(blank=True, null=True)),
                ("month_12", models.FloatField(blank=True, null=True)),
                ("month_24", models.FloatField(blank=True, null=True)),
                ("month_36", models.FloatField(blank=True, null=True)),
                ("age_filter", models.IntegerField(blank=True, default=0, null=True)),
                ("gender_filter", models.TextField(blank=True, default="", null=True)),
                ("BLSR_filter", models.TextField(blank=True, default="", null=True)),
                ("internet_filter", models.BooleanField(blank=True, null=True)),
                (
                    "deposit_joined_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="deposit_join_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "deposit_like_users",
                    models.ManyToManyField(
                        blank=True,
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
                ("join_deny", models.TextField(blank=True, null=True)),
                ("join_member", models.TextField(blank=True, null=True)),
                ("join_way", models.TextField(blank=True, null=True)),
                ("pnsn_kind_nm", models.TextField(blank=True, null=True)),
                ("prdt_type_nm", models.TextField(blank=True, null=True)),
                ("avg_prft_rate", models.FloatField(blank=True, null=True)),
                ("btrm_prft_rate_1", models.FloatField(blank=True, null=True)),
                ("btrm_prft_rate_2", models.FloatField(blank=True, null=True)),
                ("btrm_prft_rate_3", models.FloatField(blank=True, null=True)),
                ("age_filter", models.IntegerField(blank=True, default=0, null=True)),
                ("gender_filter", models.TextField(blank=True, default="", null=True)),
                ("BLSR_filter", models.TextField(blank=True, default="", null=True)),
                ("internet_filter", models.BooleanField(blank=True, null=True)),
                (
                    "annuity_joined_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="annuity_join_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "annuity_like_users",
                    models.ManyToManyField(
                        blank=True,
                        related_name="annuity_like_products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

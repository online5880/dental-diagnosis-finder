# Generated by Django 5.1 on 2024-10-15 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("search", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DentalClaim",
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
                ("incomplete_disease_code", models.CharField(max_length=50)),
                ("incomplete_disease_name", models.CharField(max_length=100)),
                (
                    "claim_category",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "claim_detail",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="insurancesubcategory",
            name="disease_codes",
        ),
        migrations.RemoveField(
            model_name="insurancesubcategory",
            name="category",
        ),
        migrations.DeleteModel(
            name="DiseaseCode",
        ),
        migrations.DeleteModel(
            name="InsuranceCategory",
        ),
        migrations.DeleteModel(
            name="InsuranceSubCategory",
        ),
    ]

# Generated by Django 4.1 on 2023-02-11 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("rate", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RateContent",
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
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("point01", models.IntegerField(default=0)),
                ("point02", models.IntegerField(default=0)),
                ("point03", models.IntegerField(default=0)),
                ("point04", models.IntegerField(default=0)),
                ("point05", models.IntegerField(default=0)),
                ("point06", models.IntegerField(default=0)),
                ("contents", models.TextField()),
                ("userId", models.CharField(max_length=20)),
                ("userPwd", models.CharField(max_length=4)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rate.category"
                    ),
                ),
                (
                    "subcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="rate.subcategory",
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2024-12-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("beasiswa", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prodi",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("prodi", models.CharField(max_length=25)),
            ],
            options={
                "verbose_name": "Prodi",
                "verbose_name_plural": "Prodi",
                "ordering": ["id"],
            },
        ),
    ]

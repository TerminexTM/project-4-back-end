# Generated by Django 3.2.6 on 2021-08-22 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_api', '0002_alter_company_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000, unique=True)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
    ]

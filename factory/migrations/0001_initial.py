# Generated by Django 4.1 on 2022-08-12 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Factory_name', models.CharField(max_length=200)),
                ('Location', models.CharField(max_length=200)),
                ('Product', models.CharField(max_length=200)),
            ],
        ),
    ]

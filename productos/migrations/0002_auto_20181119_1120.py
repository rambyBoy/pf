# Generated by Django 2.1 on 2018-11-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.AlterModelOptions(
            name='productos',
            options={'verbose_name_plural': 'Productos'},
        ),
    ]

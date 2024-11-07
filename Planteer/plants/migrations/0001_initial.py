# Generated by Django 5.1.3 on 2024-11-07 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('about', models.TextField()),
                ('used_for', models.TextField()),
                ('image', models.ImageField(default='', upload_to='images/')),
                ('native_locations', models.CharField(max_length=200)),
                ('is_edible', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Flower', 'Flower'), ('Tree', 'Tree'), ('Shrub', 'Shrub'), ('Herb', 'Herb'), ('Vegetable', 'Vegetable'), ('Fruit', 'Fruit')], max_length=20)),
            ],
        ),
    ]

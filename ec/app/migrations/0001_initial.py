# Generated by Django 5.0.3 on 2024-03-17 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('TS', 'T-Shirt'), ('S', 'Sneakers'), ('P', 'Pants'), ('H', 'Hats'), ('SW', 'Sweaters'), ('J', 'Jackets'), ('A', 'Accesories')], max_length=2)),
                ('product_image', models.ImageField(upload_to='product')),
            ],
        ),
    ]

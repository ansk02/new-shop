# Generated by Django 3.2.4 on 2021-06-13 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, unique=True, verbose_name='Nom du produit')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.FloatField(default=0, verbose_name='Prix')),
                ('images', models.ImageField(upload_to='photos/products')),
                ('stock', models.IntegerField()),
                ('is_available', models.BooleanField(default=True, verbose_name='Disponible ? ')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Dernière modification')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
            ],
            options={
                'verbose_name': 'Produit',
                'verbose_name_plural': 'Produits',
            },
        ),
        migrations.CreateModel(
            name='VariationManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_category', models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100, verbose_name='choix')),
                ('variation_value', models.CharField(max_length=100, verbose_name='couleur/taille')),
                ('is_active', models.BooleanField(default=True, verbose_name='est actif ?')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='date creation')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
            options={
                'verbose_name': 'Couleur/taille',
            },
        ),
    ]
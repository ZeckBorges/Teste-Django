# Generated by Django 5.0.2 on 2024-02-11 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemVenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venda_id', models.PositiveIntegerField()),
                ('quantidade', models.PositiveIntegerField()),
                ('preco_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto')),
            ],
        ),
    ]

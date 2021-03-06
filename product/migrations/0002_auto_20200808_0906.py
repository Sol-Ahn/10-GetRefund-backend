# Generated by Django 3.0.8 on 2020-08-08 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='applying',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Applying'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.Color'),
        ),
    ]

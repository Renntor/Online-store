# Generated by Django 4.2.4 on 2023-08-28 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_version', models.PositiveIntegerField(verbose_name='номер версии')),
                ('title_version', models.CharField(max_length=150, verbose_name='название версии')),
                ('current_version', models.BooleanField(verbose_name='признак текущий версии')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='продукт')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
            },
        ),
    ]

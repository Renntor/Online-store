# Generated by Django 4.2.4 on 2023-08-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_mail_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mail_key',
            field=models.CharField(default='O3DMt5zpseNTJqHkbXuc9Uo4Fhng2v', max_length=30, verbose_name='ключ'),
        ),
    ]

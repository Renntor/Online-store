# Generated by Django 4.2.4 on 2023-08-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='заголовок')),
                ('context', models.TextField(verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('create', models.DateField(auto_now=True, verbose_name='дата создания')),
                ('is_publish', models.BooleanField(verbose_name='статус публикации')),
                ('count_views', models.IntegerField(default=0, verbose_name='счётчик просмотров')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'блоги',
            },
        ),
    ]

# Generated by Django 4.2.1 on 2023-05-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(help_text='Cidade', max_length=32, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(help_text='Email', max_length=64, unique=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='full_name',
            field=models.CharField(help_text='Nome completo', max_length=128, verbose_name='Full name'),
        ),
    ]
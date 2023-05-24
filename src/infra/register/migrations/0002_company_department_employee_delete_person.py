# Generated by Django 4.2.1 on 2023-05-22 17:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('cnpj', models.CharField(help_text='Numero do CNPJ', max_length=14, verbose_name='CNPJ')),
                ('street', models.CharField(help_text='Logradouro,', max_length=64, verbose_name='Street')),
                ('city', models.CharField(help_text='Cidade', max_length=64, verbose_name='City')),
                ('country', models.CharField(help_text='Pais', max_length=32, verbose_name='Country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(help_text='Nome', max_length=14, verbose_name='Name')),
                ('cost_center', models.CharField(help_text='Centro de custo', max_length=64, verbose_name='Cost center')),
                ('integration_code', models.CharField(help_text='Código de integração', max_length=64, verbose_name='Integration code')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('full_name', models.CharField(help_text='Nome completo', max_length=14, verbose_name='Full name')),
                ('email', models.CharField(help_text='Email', max_length=14, verbose_name='E-mail')),
                ('phone', models.CharField(help_text='Telefone', max_length=14, verbose_name='Phone')),
                ('birthday', models.DateField(help_text='Data de aniversário', verbose_name='Birthday')),
                ('entry_date', models.DateField(help_text='Data de ingresso', verbose_name='Entry date')),
                ('departure_date', models.DateField(help_text='Data de desligamento', verbose_name='Departure date')),
                ('city', models.CharField(help_text='Cidade', max_length=14, verbose_name='City')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
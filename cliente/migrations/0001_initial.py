# Generated by Django 4.1.1 on 2022-09-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('ultima_compra', models.DateField()),
                ('endereco', models.CharField(max_length=100)),
                ('foto', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nome'],
            },
        ),
    ]

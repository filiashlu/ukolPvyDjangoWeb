# Generated by Django 3.2 on 2021-04-19 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Druh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oznaceni_druhu', models.CharField(help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný', max_length=50, unique=True, verbose_name='Označení druhu zboží')),
                ('oblast', models.CharField(blank=True, choices=[('suv', 'SUV'), ('sport', 'Sport'), ('uzitkove', 'Užitkové'), ('design', 'Designové'), ('ghetto', 'Ghetto')], default='sport', help_text='Vyberte značku', max_length=20, verbose_name='Oblast')),
            ],
            options={
                'ordering': ['oznaceni_druhu'],
            },
        ),
    ]

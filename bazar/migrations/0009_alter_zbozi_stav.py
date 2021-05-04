# Generated by Django 3.2 on 2021-05-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0008_alter_zbozi_rok'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zbozi',
            name='stav',
            field=models.IntegerField(blank=True, choices=[(5, '>200000'), (4, '<200000'), (3, '<100000'), (2, '<50000'), (1, 'Nové')], default=3, help_text='Vyberte označení stavu', verbose_name='Stav zboží'),
        ),
    ]

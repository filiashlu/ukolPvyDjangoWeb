# Generated by Django 3.2 on 2021-05-04 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0006_alter_zbozi_stav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='druh',
            name='oblast',
            field=models.CharField(blank=True, choices=[('suv', 'SUV'), ('sport', 'Sport'), ('uzitkove', 'Užitkove'), ('design', 'Designové'), ('ghetto', 'Ghetto')], default='sport', help_text='Vyberte značku', max_length=20, verbose_name='Oblast'),
        ),
        migrations.AlterField(
            model_name='zbozi',
            name='stav',
            field=models.IntegerField(blank=True, choices=[(1, '>200000'), (2, '<150000'), (3, '<100000'), (4, '<50000'), (5, 'Nové')], default=3, help_text='Vyberte označení stavu', verbose_name='Stav zboží'),
        ),
    ]
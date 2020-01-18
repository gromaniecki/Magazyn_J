# Generated by Django 3.0.2 on 2020-01-14 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0026_auto_20200114_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produkty',
            name='lokalizacja',
        ),
        migrations.AddField(
            model_name='produkty',
            name='lokacja_x',
            field=models.CharField(blank=True, choices=[('slot_1', 'Slot 1'), ('slot_2', 'Slot 2'), ('slot_3', 'Slot 3'), ('slot_4', 'Slot 4'), ('slot_5', 'Slot 5'), ('slot_6', 'Slot 6'), ('slot_7', 'Slot 7'), ('slot_9', 'Slot 9')], default='slot_1', max_length=30),
        ),
        migrations.AddField(
            model_name='produkty',
            name='regał',
            field=models.CharField(blank=True, choices=[('Regał_1', 'Regał 1'), ('Regał_2', 'Regał 2'), ('Regał_3', 'Regał 3'), ('Regał_4', 'Regał 4')], default='Regał_1', max_length=30),
        ),
        migrations.AlterField(
            model_name='produkty',
            name='półka',
            field=models.CharField(blank=True, choices=[('Półka_1', 'Półka 1'), ('Półka_2', 'Półka 2'), ('Półka_3', 'Półka 3'), ('Półka_4', 'Półka 4')], default='Półka_1', max_length=30),
        ),
    ]

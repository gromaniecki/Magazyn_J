# Generated by Django 2.2 on 2019-04-16 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0007_produkty_komentaż'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='tagi',
            field=models.ManyToManyField(blank=True, to='produkty.Tagi'),
        ),
    ]
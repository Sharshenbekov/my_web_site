# Generated by Django 4.1.4 on 2022-12-16 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruits',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='fruits',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
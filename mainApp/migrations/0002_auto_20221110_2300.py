# Generated by Django 3.2.8 on 2022-11-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='pic4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic1',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic2',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic3',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pic4',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads'),
        ),
    ]

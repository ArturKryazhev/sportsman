# Generated by Django 4.1.3 on 2022-12-14 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_product_calories_alter_product_carbo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trauma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('start', models.DateField()),
                ('end', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='diet',
            name='friday_calories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='monday_calories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='saturday_calories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='sunday_calories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='thursday_calories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='tuesday_calories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='diet',
            name='wednesday_calories',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MCQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('option1', models.CharField(max_length=255)),
                ('option2', models.CharField(max_length=255)),
                ('option3', models.CharField(max_length=255)),
                ('option4', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
    ]

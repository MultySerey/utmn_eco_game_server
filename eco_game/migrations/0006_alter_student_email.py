# Generated by Django 5.0.4 on 2024-04-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco_game', '0005_alter_student_email_alter_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
    ]
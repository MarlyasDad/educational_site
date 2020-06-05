# Generated by Django 3.0.6 on 2020-06-03 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD')], default=2),
        ),
        migrations.AlterField(
            model_name='course',
            name='start',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='time_to_read',
            field=models.PositiveSmallIntegerField(choices=[(1, '<= 1 day'), (2, '<= 1 week'), (3, '<= 1 month'), (4, '<= 6 month'), (5, '<= 1 year')], default=3),
        ),
    ]
# Generated by Django 4.1.7 on 2023-05-02 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0012_alter_student_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='timeblock',
            field=models.CharField(choices=[('A', '8:00 AM - 8:40 AM'), ('B', '8:40 AM - 9:20 AM'), ('C', '9:20 AM - 10:00 AM'), ('D', '10:00 AM - 10:40 AM'), ('E', '10:40 AM - 11:20 AM'), ('F', '11:20 AM - 12:00 PM'), ('G', '12:00 PM - 12:40 PM'), ('H', '12:40 PM - 1:20 PM'), ('I', '1:20 PM - 2:00 PM'), ('J', '2:00 PM - 2:40 PM'), ('K', '2:40 PM - 3:20 PM'), ('L', '3:20 PM - 4:00 PM'), ('M', '4:00 PM - 4:40 PM'), ('N', '4:40 PM - 5:20 PM'), ('O', '5:20 PM - 6:00 PM'), ('P', '6:00 PM - 6:40 PM'), ('Q', '6:40 PM - 7:20 PM'), ('R', '7:20 PM - 8:00 PM')], max_length=1),
        ),
    ]

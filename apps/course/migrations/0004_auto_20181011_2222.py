# Generated by Django 2.1.1 on 2018-10-11 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_ourse_org'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='ourse_org',
            new_name='Course_org',
        ),
    ]
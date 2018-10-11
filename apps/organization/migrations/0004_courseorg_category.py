# Generated by Django 2.1.1 on 2018-10-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='category',
            field=models.CharField(choices=[('pxjg', '培训机构'), ('gx', '高校'), ('gr', '个人')], default='pxjg', max_length=20, verbose_name='机构类别'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-04-29 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalapp', '0006_rename_email_jobmodel_cemail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=100)),
                ('jtitle', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('quali', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('uexp', models.CharField(choices=[('0-1', '0-1'), ('1-2', '1-2'), ('2-3', '2-3'), ('3-4', '3-4'), ('4-5', '4-5'), ('5-6', '5-6'), ('6-7', '6-7'), ('7-8', '7-8')], max_length=30)),
                ('resume', models.ImageField(upload_to='portalapp/static')),
            ],
        ),
    ]

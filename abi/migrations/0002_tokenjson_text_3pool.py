# Generated by Django 3.1.1 on 2020-09-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenjson',
            name='text_3pool',
            field=models.TextField(default=111, verbose_name='文本_3pool'),
            preserve_default=False,
        ),
    ]

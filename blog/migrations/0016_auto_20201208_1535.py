# Generated by Django 3.0.8 on 2020-12-08 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20201205_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='InternalPlag',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='grammar',
            field=models.TextField(default=None, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='onlinePlag',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_connected',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]

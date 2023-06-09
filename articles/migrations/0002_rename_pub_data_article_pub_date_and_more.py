# Generated by Django 4.2.1 on 2023-05-22 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pub_data',
            new_name='pub_date',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_title',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='Текст комментария'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-29 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_article_background_en_article_background_ja_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='background',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='background',
            name='title_ja',
        ),
        migrations.RemoveField(
            model_name='background',
            name='title_uz',
        ),
        migrations.AddField(
            model_name='about',
            name='background_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
        migrations.AddField(
            model_name='about',
            name='background_ja',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
        migrations.AddField(
            model_name='about',
            name='background_uz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.background'),
        ),
    ]
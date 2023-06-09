# Generated by Django 4.1.7 on 2023-04-13 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='books.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
    ]

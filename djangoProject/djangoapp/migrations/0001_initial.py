# Generated by Django 4.2.16 on 2024-11-14 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
                ('genre', models.CharField(choices=[('FIC', 'Fiction'), ('NON', 'Non-Fiction'), ('SCI', 'Science Fiction'), ('FAN', 'Fantasy'), ('MYS', 'Mystery'), ('THR', 'Thriller'), ('ROM', 'Romance'), ('HIS', 'Historical')], default='FIC', max_length=3)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='djangoapp.author')),
            ],
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-15 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('picture_url', models.CharField(max_length=100)),
                ('creationdate', models.DateTimeField(verbose_name='date created')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='idea',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent_idea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ideas.Idea'),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-23 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pics.Category')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='pics.Location')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]

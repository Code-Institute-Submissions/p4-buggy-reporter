# Generated by Django 2.2.4 on 2019-08-28 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_viewer', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='bug',
            name='completed_at',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]
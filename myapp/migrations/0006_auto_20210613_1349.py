# Generated by Django 3.1.1 on 2021-06-13 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_excel_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excel',
            name='pdf',
        ),
        migrations.AddField(
            model_name='pdf',
            name='excel',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.excel'),
        ),
    ]

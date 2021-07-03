# Generated by Django 3.2.4 on 2021-07-03 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_image_date_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.categories'),
        ),
        migrations.AlterField(
            model_name='image',
            name='location_taken',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.location'),
        ),
    ]

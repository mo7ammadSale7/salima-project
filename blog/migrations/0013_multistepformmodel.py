# Generated by Django 2.2.10 on 2020-12-28 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20201213_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiStepFormModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Tname', models.CharField(max_length=225)),
                ('fname', models.CharField(max_length=225)),
                ('You_are', models.CharField(max_length=225)),
                ('age', models.CharField(max_length=225)),
                ('wilaya', models.CharField(max_length=225)),
                ('fullAddress', models.CharField(max_length=225)),
                ('Email', models.CharField(max_length=225)),
                ('mainPhoneNumber', models.CharField(max_length=225)),
                ('webLink', models.CharField(max_length=225)),
                ('fbLink', models.CharField(max_length=225)),
                ('ytubeLink', models.CharField(max_length=225)),
                ('prjname', models.CharField(max_length=225)),
                ('prjfield', models.CharField(max_length=225)),
                ('prjdetail', models.CharField(max_length=225)),
                ('prjprgress', models.CharField(max_length=225)),
                ('awards', models.CharField(max_length=225)),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elevator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigungu', models.CharField(max_length=10)),
                ('elevatorNo', models.CharField(max_length=10)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('buldNm', models.CharField(max_length=100)),
                ('buldPrpos', models.CharField(max_length=30)),
                ('elvtrDivNm', models.CharField(max_length=20)),
                ('elvtrKindNm', models.CharField(max_length=15)),
                ('elvtrModel', models.CharField(max_length=20)),
                ('elvtrMgtNo1', models.IntegerField()),
                ('elvtrMgtNo2', models.IntegerField()),
                ('elvtrStts', models.CharField(max_length=10)),
                ('liveLoad', models.CharField(max_length=15)),
                ('manufacturerName', models.CharField(max_length=30)),
                ('ratedCap', models.CharField(max_length=10)),
                ('shuttleFloorCnt', models.FloatField()),
            ],
        ),
    ]

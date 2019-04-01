# Generated by Django 2.1.7 on 2019-03-31 16:51

import SmartCommunity_1622441019.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SmartCommunity_1622441019', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider_1622441019',
            fields=[
                ('providerID', models.AutoField(db_column='providerID', primary_key=True, serialize=False)),
                ('providerName', models.CharField(blank=True, db_column='providerName', max_length=60, null=True)),
                ('phoneNumber', models.CharField(blank=True, db_column='phoneNumber', max_length=45, null=True)),
                ('emailAddress', models.CharField(blank=True, db_column='emailAddress', max_length=80, null=True)),
                ('providerPrice', models.CharField(blank=True, db_column='providerPrice', max_length=6, null=True)),
                ('providerType', SmartCommunity_1622441019.models.EnumField(choices=[('Please choose your Type', 'Please choose your type'), ('Water', 'Water'), ('Electronic', 'Electronic'), ('Car', 'Car'), ('Air', 'Air'), ('Fire', 'Fire'), ('House', 'House'), ('Clean', 'Clean')], default=0)),
            ],
            options={
                'db_table': 'provider',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admin_1622441019',
            fields=[
                ('adminID', models.AutoField(db_column='adminID', primary_key=True, serialize=False)),
                ('emailAddress', models.EmailField(db_column='emailAddress', max_length=80, null=True)),
                ('firstName', models.CharField(blank=True, db_column='firstName', max_length=40, null=True)),
                ('lastName', models.CharField(blank=True, db_column='lastName', max_length=40, null=True)),
                ('password', models.CharField(blank=True, db_column='password', max_length=400, null=True)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Issue_1622441019',
            fields=[
                ('issueID', models.AutoField(db_column='issueID', primary_key=True, serialize=False)),
                ('issueName', models.CharField(blank=True, db_column='issueName', max_length=60, null=True)),
                ('address', models.CharField(blank=True, db_column='address', max_length=80, null=True)),
                ('phoneNumber', models.CharField(blank=True, db_column='phoneNumber', max_length=45, null=True)),
                ('emailAddress', models.CharField(blank=True, db_column='emailAddress', max_length=80, null=True)),
                ('issueDetail', models.CharField(blank=True, db_column='issueDetail', max_length=600, null=True)),
                ('issueType', SmartCommunity_1622441019.models.EnumField(choices=[('Please choose your Type', 'Please choose your type'), ('Water', 'Water'), ('Electronic', 'Electronic'), ('Car', 'Car'), ('Air', 'Air'), ('Fire', 'Fire'), ('House', 'House'), ('Clean', 'Clean')], default=0)),
            ],
            options={
                'db_table': 'issue',
            },
        ),
        migrations.CreateModel(
            name='PrviderType_1622441019',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prviderType', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User_1622441019',
            fields=[
                ('userID', models.AutoField(db_column='userID', primary_key=True, serialize=False)),
                ('emailAddress', models.EmailField(db_column='emailAddress', max_length=80, null=True)),
                ('firstName', models.CharField(blank=True, db_column='firstName', max_length=40, null=True)),
                ('lastName', models.CharField(blank=True, db_column='lastName', max_length=40, null=True)),
                ('phoneNumber', models.CharField(blank=True, db_column='phoneNumber', max_length=45, null=True)),
                ('userType', SmartCommunity_1622441019.models.EnumField(choices=[('Please choose your user type', 'Please choose your user type'), ('Member', 'Member'), ('Volunteer', 'Volunteer')], default=0)),
                ('password', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
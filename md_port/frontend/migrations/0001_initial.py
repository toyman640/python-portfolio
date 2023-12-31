# Generated by Django 4.1.2 on 2023-07-15 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_name', models.CharField(max_length=100, verbose_name='Award Name')),
                ('award_org', models.CharField(max_length=100, verbose_name='Organization/Body')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('org_image', models.ImageField(upload_to='uploads/', verbose_name='Body logo')),
            ],
        ),
        migrations.CreateModel(
            name='FirstQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Name')),
                ('first_quote', models.TextField(blank=True, verbose_name='First Quote')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_name', models.CharField(max_length=100, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('subject', models.CharField(max_length=100, verbose_name='Subject')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=100, verbose_name='Project title')),
                ('project_date', models.IntegerField(max_length=100, verbose_name='Project date')),
                ('project_description', models.TextField(blank=True, verbose_name='message')),
                ('test_image1', models.ImageField(upload_to='uploads/', verbose_name='Image1')),
                ('test_image2', models.ImageField(upload_to='uploads/', verbose_name='Image2')),
                ('test_image3', models.ImageField(upload_to='uploads/', verbose_name='Image3')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=100, verbose_name='Name')),
                ('title', models.CharField(max_length=100, verbose_name='title/position')),
                ('message', models.TextField(blank=True, verbose_name='message')),
                ('test_image', models.ImageField(upload_to='uploads/', verbose_name='Image')),
            ],
        ),
    ]

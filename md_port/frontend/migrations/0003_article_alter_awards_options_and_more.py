# Generated by Django 4.1.2 on 2023-07-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_awards_id_alter_firstquote_id_alter_message_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('art_titile', models.CharField(max_length=100, verbose_name='Article title')),
                ('post', models.TextField(blank=True, verbose_name='Post')),
                ('art_image', models.ImageField(upload_to='uploads/', verbose_name='Image3')),
            ],
            options={
                'verbose_name_plural': 'Article Title',
            },
        ),
        migrations.AlterModelOptions(
            name='awards',
            options={'verbose_name_plural': 'Award Name'},
        ),
        migrations.AlterModelOptions(
            name='firstquote',
            options={'verbose_name_plural': 'Quote'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': 'Email'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Project title'},
        ),
        migrations.AlterModelOptions(
            name='testimonials',
            options={'verbose_name_plural': 'Testimonial name'},
        ),
    ]

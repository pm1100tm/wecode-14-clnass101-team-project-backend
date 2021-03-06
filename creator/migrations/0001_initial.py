# Generated by Django 3.1.5 on 2021-01-20 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryChapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thumbnail_image', models.URLField(null=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'db_table': 'temporary_chapters',
            },
        ),
        migrations.CreateModel(
            name='TemporaryKit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'temporary_kits',
            },
        ),
        migrations.CreateModel(
            name='TemporaryKitImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
            ],
            options={
                'db_table': 'temporary_kit_images',
            },
        ),
        migrations.CreateModel(
            name='TemporaryLecture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('video_url', models.URLField(null=True)),
                ('duration', models.DurationField(null=True)),
                ('order', models.IntegerField()),
            ],
            options={
                'db_table': 'temporary_lectures',
            },
        ),
        migrations.CreateModel(
            name='TemporaryLectureContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
            ],
            options={
                'db_table': 'temporary_lecture_contents',
            },
        ),
        migrations.CreateModel(
            name='TemporaryLectureContentDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'temporary_lecture_content_descriptions',
            },
        ),
        migrations.CreateModel(
            name='TemporaryLectureContentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'temporary_lecture_content_images',
            },
        ),
        migrations.CreateModel(
            name='TemporaryProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('sale', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'temporary_products',
            },
        ),
        migrations.CreateModel(
            name='TemporaryProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('temporary_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.temporaryproduct')),
            ],
            options={
                'db_table': 'temporary_product_images',
            },
        ),
    ]

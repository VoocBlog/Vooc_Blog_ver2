# Generated by Django 3.0.4 on 2020-03-27 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_post', models.CharField(max_length=200)),
                ('pub_date_post', models.DateTimeField(auto_now_add=True)),
                ('body_post', models.TextField()),
                ('image_post', models.ImageField(null=True, upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='roles.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_cmt', models.TextField()),
                ('date_cmt', models.DateTimeField(auto_now_add=True)),
                ('is_like', models.IntegerField(default=0)),
                ('like_amount', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roles.Post')),
            ],
        ),
    ]

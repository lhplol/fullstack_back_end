# Generated by Django 5.0.7 on 2024-08-05 03:58

import common.core.models
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Created time')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='Updated time')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='Description')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='', verbose_name='书籍封面')),
                ('book_file', models.FileField(blank=True, null=True, upload_to=common.core.models.upload_directory_path, verbose_name='书籍存储')),
                ('name', models.CharField(help_text='书籍名称啊，随便填', max_length=100, verbose_name='书籍名称')),
                ('isbn', models.CharField(max_length=20, verbose_name='标准书号')),
                ('author', models.CharField(help_text='坐着大啊啊士大夫', max_length=20, verbose_name='书籍作者')),
                ('publisher', models.CharField(default='大宇出版社', max_length=20, verbose_name='出版社')),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='出版日期')),
                ('price', models.FloatField(default=999.99, verbose_name='书籍售价')),
                ('is_active', models.BooleanField(default=False, verbose_name='是否启用')),
                ('category', models.SmallIntegerField(choices=[(0, '小说'), (1, '文学'), (2, '哲学')], default=0, verbose_name='书籍类型')),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='管理员')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='creator_query', to=settings.AUTH_USER_MODEL, verbose_name='Creator')),
                ('dept_belong', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='dept_belong_query', to='system.deptinfo', verbose_name='Data ownership department')),
                ('modifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', related_query_name='modifier_query', to=settings.AUTH_USER_MODEL, verbose_name='Modifier')),
            ],
            options={
                'verbose_name': '书籍名称',
                'verbose_name_plural': '书籍名称',
            },
        ),
    ]

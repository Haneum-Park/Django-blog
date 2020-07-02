# Generated by Django 3.0.6 on 2020-06-29 01:44

from django.db import migrations, models
import django.db.models.deletion
import tagging.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='카테고리 ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='카테고리명')),
                ('parent_value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Categories', verbose_name='부모아이디')),
            ],
            options={
                'db_table': 'CATEGORIES',
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='최대 200자 내로 입력하세요.', max_length=200, verbose_name='제목')),
                ('contents', models.TextField(verbose_name='내용')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='조회수')),
                ('tags', tagging.fields.TagField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_username', to='accounts.User', to_field='username')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='posts.Categories')),
                ('likes_user', models.ManyToManyField(blank=True, related_name='likes_user', to='accounts.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='accounts.User')),
            ],
            options={
                'db_table': 'POSTS',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(verbose_name='내용')),
                ('arrived_date', models.DateTimeField(auto_now_add=True)),
                ('from_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='보낸사람', to='accounts.User', to_field='username')),
                ('to_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='받는사람', to='accounts.User', to_field='username')),
            ],
            options={
                'db_table': 'NOTE',
            },
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrived_date', models.DateTimeField(auto_now_add=True)),
                ('mail_from_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='메일보낸사람', to='accounts.User', to_field='username')),
                ('mail_to_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='메일받는사람', to='accounts.User', to_field='username')),
            ],
            options={
                'db_table': 'MAIL',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, verbose_name='이름')),
                ('comment', models.TextField(default='', verbose_name='댓글')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Comments', verbose_name='대댓글')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Posts')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User')),
                ('username', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Comments.username+', to='accounts.User', to_field='username', verbose_name='닉네임')),
            ],
            options={
                'db_table': 'COMMENTS',
            },
        ),
    ]

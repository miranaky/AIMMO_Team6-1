# Generated by Django 3.2.9 on 2021-11-02 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(help_text='Comment', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='created time', verbose_name='created_time')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='updated time', null=True)),
                ('parent', models.ForeignKey(blank=True, help_text='Check_parent_comment', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='comments.comment')),
            ],
        ),
    ]

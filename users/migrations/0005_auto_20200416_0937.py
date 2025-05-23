# Generated by Django 3.0.4 on 2020-04-16 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200409_0849'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userexpertise',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='user',
            name='membership_platform_type',
            field=models.CharField(choices=[('patreon', 'Patreon')], default='patreon', max_length=128),
        ),
        migrations.AlterField(
            model_name='user',
            name='membership_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('pro', 'Pro'), ('lifetime', 'Lifetime')], default='normal', max_length=16),
        ),
        migrations.AlterField(
            model_name='userexpertise',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expertise', to='users.User'),
        ),
    ]

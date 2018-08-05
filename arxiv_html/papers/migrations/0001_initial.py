# Generated by Django 2.0.7 on 2018-08-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Render',
            fields=[
                ('id_type', models.CharField(choices=[('arxiv', 'arXiv'), ('submission', 'Submission')], max_length=20)),
                ('paper_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('state', models.CharField(choices=[('unstarted', 'Unstarted'), ('running', 'Running'), ('success', 'Success'), ('failure', 'Failure')], default='unstarted', max_length=20)),
                ('logs', models.TextField(blank=True, null=True)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
    ]
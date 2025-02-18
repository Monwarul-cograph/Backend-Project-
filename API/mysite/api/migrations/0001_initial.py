# Generated by Django 5.0.6 on 2024-09-03 04:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyList',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('更新日', models.DateField(max_length=255, verbose_name='更新日')),
                ('名称', models.CharField(max_length=255, verbose_name='名称')),
                ('業界_小分類', models.CharField(blank=True, max_length=255, null=True, verbose_name='業界_小分類')),
                ('求人有無', models.CharField(max_length=255, verbose_name='求人有無')),
                ('事業内容', models.TextField(verbose_name='事業内容')),
                ('所在地', models.CharField(max_length=255, verbose_name='所在地')),
                ('設立', models.IntegerField(blank=True, null=True, verbose_name='設立')),
                ('従業員数', models.IntegerField(blank=True, null=True, verbose_name='従業員数')),
                ('資本金', models.CharField(blank=True, max_length=20, null=True, verbose_name='資本金')),
                ('企業URL', models.URLField(blank=True, max_length=1000, null=True, verbose_name='企業URL')),
                ('上場市場名', models.CharField(blank=True, max_length=255, null=True, verbose_name='上場市場名')),
                ('代表者', models.CharField(blank=True, max_length=255, null=True, verbose_name='代表者')),
                ('平均年齢', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='平均年齢')),
                ('お問い合わせ先URL', models.URLField(blank=True, max_length=1000, null=True, verbose_name='お問い合わせ先URL')),
                ('代表電話番号', models.CharField(blank=True, max_length=20, null=True, verbose_name='代表電話番号')),
            ],
        ),
        migrations.CreateModel(
            name='CEONumberID',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('代表電話番号', models.CharField(blank=True, max_length=20, null=True, verbose_name='代表電話番号')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ceo_numbers', to='api.companylist')),
            ],
        ),
        migrations.CreateModel(
            name='AddressID',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('所在地', models.CharField(max_length=255, verbose_name='所在地')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='api.companylist')),
            ],
        ),
        migrations.CreateModel(
            name='HomePageID',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('企業URL', models.URLField(blank=True, max_length=1000, null=True, verbose_name='企業URL')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homepage_urls', to='api.companylist')),
            ],
        ),
        migrations.CreateModel(
            name='JobList',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('JOB_TITTLE', models.CharField(max_length=255, verbose_name='JOB Tittle')),
                ('JOB_DESCRIPTION', models.CharField(max_length=255, verbose_name='JOB Description')),
                ('LOCATION', models.TextField(verbose_name='Location')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_list', to='api.companylist')),
            ],
        ),
        migrations.CreateModel(
            name='URLID',
            fields=[
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('お問い合わせ先URL', models.URLField(blank=True, max_length=1000, null=True, verbose_name='お問い合わせ先URL')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='urls', to='api.companylist')),
            ],
        ),
    ]

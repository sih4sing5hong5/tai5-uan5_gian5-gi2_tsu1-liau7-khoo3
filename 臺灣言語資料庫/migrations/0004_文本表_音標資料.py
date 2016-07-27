# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 02:06
from __future__ import unicode_literals

from django.db import migrations, models


def _文本的屬性音標徙去音標資料(apps, schema_editor):
    文本表 = apps.get_model("臺灣言語資料庫", "文本表")
    for 文本 in 文本表.objects.filter(屬性__分類='音標'):
        音標屬性 = 文本.屬性.get(分類='音標')
        文本.音標資料 = 音標屬性.性質
        文本.save()
        文本.屬性.remove(音標屬性)


def _文本的音標資料徙轉屬性音標(apps, schema_editor):
    文本表 = apps.get_model("臺灣言語資料庫", "文本表")
    for 文本 in 文本表.objects.exclude(音標資料=''):
        try:
            音標欄位 = 文本.屬性.get(分類='音標')
            文本.屬性.remove(音標欄位)
        except:
            pass
        文本.屬性.get_or_create(分類='音標', 性質=文本.音標資料)
        文本.save()


class Migration(migrations.Migration):

    dependencies = [
        ('臺灣言語資料庫', '0003_auto_20151009_0731_版權加長度'),
    ]

    operations = [
        migrations.AddField(
            model_name='文本表',
            name='音標資料',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.RunPython(
            _文本的屬性音標徙去音標資料,
            _文本的音標資料徙轉屬性音標,
        ),
        migrations.AlterField(
            model_name='文本表',
            name='音標資料',
            field=models.TextField(blank=True),
        ),
    ]

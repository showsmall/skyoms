# Generated by Django 3.1.2 on 2020-10-22 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('users', '0002_auto_20201017_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermenu',
            name='permission',
            field=models.ForeignKey(blank=True, help_text='$显示字段$__name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.permission', verbose_name='菜单关联权限'),
        ),
        migrations.AlterField(
            model_name='userrouter',
            name='permission',
            field=models.ForeignKey(blank=True, help_text='$显示字段$__name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.permission', verbose_name='路由关联权限'),
        ),
    ]
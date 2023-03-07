# Generated by Django 4.1.6 on 2023-03-06 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_ratecontent_isapproval_ratecontent_schpwd'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolPwd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('schPwd', models.CharField(default='0000', max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='ratecontent',
            name='schPwd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate.schoolpwd'),
        ),
    ]
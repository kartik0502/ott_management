# Generated by Django 4.1.3 on 2022-11-19 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_alter_employee_admin_id_alter_subscribers_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='admin_id',
            field=models.ForeignKey(db_column='admin_id', on_delete=django.db.models.deletion.CASCADE, to='database.administrator'),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='database.user'),
        ),
        migrations.AlterField(
            model_name='user',
            name='employee_id',
            field=models.ForeignKey(db_column='employee_id', on_delete=django.db.models.deletion.CASCADE, to='database.employee'),
        ),
    ]
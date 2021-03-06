# Generated by Django 3.2 on 2022-07-16 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('language', models.CharField(choices=[('ua', 'Українська мова'), ('ru', 'Русский язык')], default='ru', max_length=10)),
                ('sex', models.CharField(choices=[('male', 'Мужской пол'), ('female', 'Женский пол')], max_length=15)),
                ('phone_number', models.CharField(max_length=20)),
                ('born', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='MailingStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('many_of_sended_list', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.CharField(choices=[('booking', 'бронь'), ('buying', 'покупка')], max_length=20)),
                ('plase', models.JSONField()),
                ('show', models.ForeignKey(on_delete=models.SET('Сеанс отменен, свяжитесь с администрацией кинотеатра'), to='cinema.show')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.customuser')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='letters',
            field=models.ManyToManyField(to='users.Mailing'),
        ),
    ]

# Generated by Django 2.0.4 on 2018-04-14 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='DegreeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='名称')),
                ('course_img', models.CharField(max_length=255, verbose_name='缩略图')),
                ('brief', models.TextField(verbose_name='学位课程简介')),
                ('total_scholarship', models.PositiveIntegerField(default=40000, verbose_name='总奖学金(贝里)')),
                ('mentor_compensation_bonus', models.PositiveIntegerField(default=15000, verbose_name='本课程的导师辅导费用(贝里)')),
                ('period', models.PositiveIntegerField(default=150, help_text='为了计算学位奖学金', verbose_name='建议学习周期(days)')),
                ('prerequisite', models.TextField(max_length=1024, verbose_name='课程先修要求')),
            ],
            options={
                'verbose_name': '学位课程',
                'verbose_name_plural': '学位课程',
            },
        ),
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(verbose_name='关联普通课或者学位课中的课程ID')),
                ('valid_period', models.SmallIntegerField(choices=[(1, '1天'), (3, '3天'), (7, '1周'), (14, '2周'), (30, '1个月'), (60, '2个月'), (90, '3个月'), (180, '6个月'), (210, '12个月'), (540, '18个月'), (720, '24个月')], verbose_name='课程周期')),
                ('price', models.FloatField(verbose_name='价格')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='关联普通课或者学位课表')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('role', models.SmallIntegerField(choices=[(1, '讲师'), (2, '导师')], default=1)),
                ('title', models.CharField(max_length=64, verbose_name='职位、职称')),
                ('signature', models.CharField(blank=True, max_length=255, null=True, verbose_name='导师签名')),
                ('image', models.CharField(max_length=128, verbose_name='头像')),
                ('brief', models.TextField(max_length=1024, verbose_name='简介')),
            ],
            options={
                'verbose_name': '讲师导师',
                'verbose_name_plural': '讲师导师',
            },
        ),
        migrations.AddField(
            model_name='degreecourse',
            name='teachers',
            field=models.ManyToManyField(to='luffy.Teacher', verbose_name='课程讲师'),
        ),
        migrations.AlterUniqueTogether(
            name='pricepolicy',
            unique_together={('content_type', 'object_id', 'valid_period')},
        ),
    ]

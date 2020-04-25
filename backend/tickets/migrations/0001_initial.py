# Generated by Django 3.0.2 on 2020-04-23 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workflows', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(blank=True, default='', help_text='工单的标题', max_length=112, verbose_name='标题')),
                ('sn', models.CharField(help_text='工单的流水号', max_length=25, verbose_name='流水号')),
                ('participant_type', models.CharField(choices=[(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色')], default=0, max_length=1, verbose_name='当前处理人类型')),
                ('participant', models.CharField(blank=True, default='', help_text='可以为空(无处理人的情况，如结束状态)、username\\多个username(以,隔开)\\部门id\\角色id\\脚本文件名等', max_length=100, verbose_name='当前处理人')),
                ('relation', models.CharField(blank=True, default='', help_text='工单流转过程中将保存所有相关的人(包括创建人、曾经的待处理人)，用于查询', max_length=255, verbose_name='工单关联人')),
                ('act_state', models.CharField(choices=[(0, '草稿中'), (1, '进行中'), (2, '被退回'), (3, '被撤回'), (4, '已完成'), (5, '已关闭')], default=0, max_length=1, verbose_name='进行状态')),
                ('multi_all_person', models.TextField(default='{}', help_text='需要当前状态处理人全部处理时实际的处理结果，json格式', verbose_name='全部处理的结果')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.State', verbose_name='当前状态')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Workflow', verbose_name='工作流')),
            ],
            options={
                'verbose_name': '工单记录',
                'verbose_name_plural': '工单记录',
            },
        ),
        migrations.CreateModel(
            name='TicketUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('username', models.CharField(max_length=100, verbose_name='关系人')),
                ('in_process', models.BooleanField(default=False, verbose_name='待处理中')),
                ('worked', models.BooleanField(default=False, verbose_name='处理过')),
                ('ticket', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.Ticket')),
            ],
            options={
                'verbose_name': '工单关系人',
                'verbose_name_plural': '工单关系人',
            },
        ),
        migrations.CreateModel(
            name='TicketFlowLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('suggestion', models.TextField(blank=True, default='', verbose_name='处理意见')),
                ('participant_type', models.CharField(choices=[(0, '无处理人'), (1, '个人'), (2, '多人'), (3, '部门'), (4, '角色')], default=0, max_length=1, verbose_name='处理人类型')),
                ('participant', models.CharField(blank=True, default='', max_length=50, verbose_name='处理人')),
                ('intervene_type', models.CharField(choices=[(0, '转交操作'), (1, '接单操作'), (2, '评论操作'), (3, '删除操作'), (4, '强制关闭操作'), (5, '强制修改状态操作'), (6, '撤回')], default=0, max_length=1, verbose_name='干预类型')),
                ('ticket_data', models.TextField(blank=True, default='', help_text='可以用于记录当前表单数据，json格式', verbose_name='工单数据')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.State', verbose_name='当前状态')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket', verbose_name='工单')),
                ('transition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflows.Transition', verbose_name='流转')),
            ],
            options={
                'verbose_name': '工单流转日志',
                'verbose_name_plural': '工单流转日志',
            },
        ),
        migrations.CreateModel(
            name='TicketCustomField',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('memo', models.TextField(blank=True, verbose_name='备注')),
                ('name', models.CharField(max_length=50, verbose_name='字段名')),
                ('field_key', models.CharField(max_length=50, verbose_name='字段标识')),
                ('field_type', models.CharField(choices=[(5, '字符串'), (10, '整形'), (15, '浮点型'), (20, '布尔'), (25, '日期'), (30, '时间'), (35, '日期时间'), (40, '单选框'), (45, '多选框'), (50, '下拉列表'), (55, '多选下拉列表'), (60, '文本域'), (65, '用户名'), (70, '多选的用户名')], default=0, max_length=1, verbose_name='字段类型')),
                ('char_value', models.CharField(blank=True, default='', max_length=255, verbose_name='字符串值')),
                ('int_value', models.IntegerField(blank=True, default=0, verbose_name='整形值')),
                ('float_value', models.FloatField(blank=True, default=0.0, verbose_name='浮点值')),
                ('bool_value', models.BooleanField(blank=True, default=False, verbose_name='布尔值')),
                ('date_value', models.DateField(auto_now_add=True, verbose_name='日期值')),
                ('datetime_value', models.DateTimeField(auto_now_add=True, verbose_name='日期时间值')),
                ('time_value', models.TimeField(auto_now_add=True, verbose_name='时间值')),
                ('radio_value', models.CharField(blank=True, default='', max_length=50, verbose_name='radio值')),
                ('checkbox_value', models.CharField(blank=True, default='', help_text='逗号隔开多个选项', max_length=50, verbose_name='checkbox值')),
                ('select_value', models.CharField(blank=True, default='', max_length=50, verbose_name='下拉列表值')),
                ('multi_select_value', models.CharField(blank=True, default='', help_text='逗号隔开多个选项', max_length=50, verbose_name='多选下拉列表值')),
                ('text_value', models.TextField(blank=True, default='', verbose_name='文本值')),
                ('username_value', models.CharField(blank=True, default='', max_length=50, verbose_name='用户名')),
                ('multi_username_value', models.CharField(blank=True, default='', max_length=255, verbose_name='多选用户名')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket', verbose_name='工单')),
            ],
            options={
                'verbose_name': '工单自定义字段',
                'verbose_name_plural': '工单自定义字段',
            },
        ),
    ]
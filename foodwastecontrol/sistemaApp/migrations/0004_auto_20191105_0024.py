# Generated by Django 2.2.6 on 2019-11-05 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaApp', '0003_desperdicio_refeicao_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_alimento', models.CharField(max_length=30)),
                ('valor_alimento', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.RenameField(
            model_name='refeicao',
            old_name='id_empresa',
            new_name='empresa',
        ),
        migrations.RenameField(
            model_name='refeicao',
            old_name='id_usuario',
            new_name='usuario',
        ),
        migrations.RemoveField(
            model_name='refeicao',
            name='valor_alimento',
        ),
        migrations.AddField(
            model_name='refeicao',
            name='alimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='sistemaApp.Alimento'),
        ),
    ]

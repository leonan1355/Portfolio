# Generated by Django 5.0.7 on 2024-08-24 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('condicoes_ativacao', models.JSONField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='classes/')),
            ],
        ),
        migrations.CreateModel(
            name='Campeao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('custo', models.IntegerField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='campeoes/')),
                ('classes', models.ManyToManyField(related_name='campeoes', to='tftbuilder.classe')),
            ],
        ),
    ]

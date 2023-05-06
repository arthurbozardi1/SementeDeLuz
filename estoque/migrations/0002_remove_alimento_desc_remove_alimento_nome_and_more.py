# Generated by Django 4.1.2 on 2022-10-28 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alimento',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='alimento',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='higiene',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='higiene',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='roupa',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='roupa',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='roupacama',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='roupacama',
            name='nome',
        ),
        migrations.AddField(
            model_name='alimento',
            name='descr',
            field=models.CharField(choices=[('1', 'Carboidrato'), ('2', 'sei la'), ('3', 'Pasta de dentes'), ('4', 'Papel Higiênico')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='higiene',
            name='condicao',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], null=True),
        ),
        migrations.AddField(
            model_name='higiene',
            name='descr',
            field=models.CharField(choices=[('1', 'Sabonete'), ('2', 'Escova de dentes'), ('3', 'Pasta de dentes'), ('4', 'Papel Higiênico')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='higiene',
            name='vencimento',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='roupa',
            name='condicao',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], null=True),
        ),
        migrations.AddField(
            model_name='roupa',
            name='descr',
            field=models.CharField(choices=[('1', 'Calça'), ('2', 'Casaco'), ('3', 'Camiseta'), ('4', 'Camisa')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='roupacama',
            name='descr',
            field=models.CharField(choices=[('1', 'Lençol'), ('2', 'Cobertor'), ('3', 'Fronha'), ('4', 'sei la')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='qntd',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='alimento',
            name='vencimento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='senha',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='sobrenome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='telefone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='higiene',
            name='qntd',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='sobrenome',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='integrante',
            name='telefone',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='cor',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='qntd',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupa',
            name='tamanho',
            field=models.CharField(choices=[('1', 'P'), ('2', 'M'), ('3', 'G'), ('4', 'GG')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='roupacama',
            name='qntd',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='roupacama',
            name='tamanho',
            field=models.CharField(choices=[('1', 'Solteiro'), ('2', 'Casal'), ('3', 'QueenSize'), ('4', 'KingSize')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='Produto',
        ),
    ]

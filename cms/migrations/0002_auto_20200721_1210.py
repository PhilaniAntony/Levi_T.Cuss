# Generated by Django 3.0.8 on 2020-07-21 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=450, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Deactived', 'Deactived')], max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='productType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shippers',
            name='Order',
            field=models.ManyToManyField(to='cms.Order'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='product',
            field=models.ManyToManyField(to='cms.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='collection',
            field=models.ManyToManyField(to='cms.Collection'),
        ),
    ]

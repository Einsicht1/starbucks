# Generated by Django 3.0.7 on 2020-06-13 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0004_category_drink_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergies',
            },
        ),
        migrations.CreateModel(
            name='Nutrition_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serviong_kcal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=5)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'db_table': 'nutrition_informations',
            },
        ),
        migrations.RenameField(
            model_name='drink',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='drink_id',
            new_name='drink',
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('size_mi', models.IntegerField(default=0)),
                ('size_fluid_ounce', models.IntegerField(default=0)),
                ('nutrition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Nutrition_Information')),
            ],
            options={
                'db_table': 'sizes',
            },
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Drink')),
            ],
            options={
                'db_table': 'descriptions',
            },
        ),
        migrations.CreateModel(
            name='Allergy_Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Drink')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='table.Allergy')),
            ],
            options={
                'db_table': 'allergy_drinks',
            },
        ),
        migrations.AddField(
            model_name='drink',
            name='nutrition_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='table.Nutrition_Information'),
            preserve_default=False,
        ),
    ]
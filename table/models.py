from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "categories"

class Drink(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    nutrition_id = models.ForeignKey('Nutrition_Information', on_delete=models.CASCADE)

    class Meta:
        db_table ='drinks'


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Description(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)

    class Meta:
        db_table = 'descriptions'


class Nutrition_Information(models.Model):
    one_serving_kcal = models.DecimalField(max_digits=5, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=2) 
    protein_g = models.DecimalField(max_digits=5, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'nutrition_informations'


class Size(models.Model):
    nutrition = models.ForeignKey('Nutrition_Information', on_delete=models.CASCADE) 
    name = models.CharField(max_length=45)
    size_mi = models.IntegerField(default=0)
    size_fluid_ounce = models.IntegerField(default=0)
    

    class Meta:
        db_table = 'sizes'



class Allergy(models.Model):
    name = models.CharField(max_length=45)
    
    class Meta:
        db_table = "allergies"


class Allergy_Drink(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = "allergy_drinks"

# Create your models here.

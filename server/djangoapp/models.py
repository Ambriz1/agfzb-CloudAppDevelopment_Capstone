from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
class CarMake(models.Model):
    name = models.CharField(max_length=100, default="make")
    description = models.CharField(max_length=100, default="description")
    origin = models.CharField(max_length=100, default="country of origin")

    def __str__(self):
        return self.name
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name_model = models.CharField(max_length=100, default="car model")
    dealer_id = models.IntegerField(default="0")
    year = models.DateField()
    TYPE = [
        ('Car', 'Car'),
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Van', 'Van'),
        ('Wagon', 'Wagon'),
        ('Other', 'Other')
    ]
    car_type = models.CharField(max_length=20, choices=TYPE, default="choose a type")
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
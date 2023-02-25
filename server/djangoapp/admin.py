from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# CarModelAdmin class

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'name_model', 'dealer_id', 'year', 'car_type')
    list_filter = ['car_make']
    search_fields = ('year', 'car_type')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description', 'origin')
    search_fields = ('name', 'origin')
# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
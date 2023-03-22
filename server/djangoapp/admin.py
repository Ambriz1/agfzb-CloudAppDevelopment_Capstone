from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 1

# CarModelAdmin class

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('car_make', 'car_model', 'dealer_id', 'year', 'car_type')
    list_filter = ['car_make']
    search_fields = ('year', 'car_type')

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('car_make', 'description', 'origin')
    search_fields = ('car_make', 'origin')
# Register models here
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarMake, CarMakeAdmin)
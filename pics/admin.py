from django.contrib import admin
from .models import Image,location,Category

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('location',)

admin.site.register(Image)
admin.site.register(location)
admin.site.register(Category,CategoryAdmin)



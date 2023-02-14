from django.contrib import admin
from .models import Category, SubCategory, RateContent

class SubCategooryInline(admin.StackedInline):
    model = SubCategory
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category Order', {'fields': ['category_order']}),
        (None,               {'fields': ['category_name']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [SubCategooryInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory)
admin.site.register(RateContent)

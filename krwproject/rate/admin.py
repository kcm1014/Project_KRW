from django.contrib import admin
from .models import Category, SubCategory, RateContent, SchoolPwd

class SubCategooryInline(admin.StackedInline):
    model = SubCategory
    extra = 5

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_order', 'category_name', 'pub_date']

    fieldsets = [
        ('Category Order', {'fields': ['category_order']}),
        (None,               {'fields': ['category_name']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [SubCategooryInline]

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'subcategory_order', 'subcategory_name', 'subcategory','category_name']
    def category_name(self, obj):
        if obj.subcategory:
            return obj.subcategory.category_name

    category_name.short_description = "Category Name"
@admin.register(RateContent)
class RateContentAddmin(admin.ModelAdmin):
    list_display = ['id','category_name','subcategory_name','isApproval','create_date', 'point01', 'point02','point03','point04','point05','point06','contents','userId','userPwd','schPwd']

    def category_name(self, obj):
        if obj.category:
            return obj.category.category_name

    def subcategory_name(self, obj):
        if obj.subcategory:
            return obj.subcategory.subcategory_name

    category_name.short_description="Category Name"
    subcategory_name.short_description ="Subcategory Name"
@admin.register(SchoolPwd)
class SchoolPwdAdmin(admin.ModelAdmin):
    list_display = ['id', 'create_date', 'schPwd']
#,
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(SubCategory)
#admin.site.register(RateContent)
#admin.site.register(SchoolPwd)

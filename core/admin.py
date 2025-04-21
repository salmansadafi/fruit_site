from django.contrib import admin
from core.models import Contact,Subscribe,Product,Team
# Register your models here.





# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_date',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'created_date')
    search_fields = ('title', 'description')
    list_filter = ('created_date',)


admin.site.register(Contact,ContactAdmin)
admin.site.register(Subscribe)
admin.site.register(Product,ProductAdmin)
admin.site.register(Team)
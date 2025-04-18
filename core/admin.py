from django.contrib import admin
from core.models import Contact,Newsletter
# Register your models here.





# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_date')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_date',)


admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)
from django.contrib import admin
from blog.models import Post,Comment,Category

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy ="created_date"  # Adds a date-based drill-down navigation in the admin list view
    empty_value_display = "-empty-"  # Customizes the display of empty values in the admin list view
    #fields = ('title',)  # Specifies the fields to display in the form view for the Post model
    list_display = ('title','status','author', 'counted_views', 'created_date' , 'published_date')  # Specifies the fields to display in the list view for the Post model
    list_filter =('status',)  # Adds a filter sidebar to the admin list view. حتما باید نوعش تاپل باشه یعنی اخرش کاما باشه
    search_fields = ['title', 'content']  # Adds a search box to the admin list view

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_date', 'approved')
    list_filter = ('approved', 'created_date')
    search_fields = ('name', 'message')

admin.site.register(Post,PostAdmin) #--> @admin.register(Post)
#admin.site.register(Category)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Category)
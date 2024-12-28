from django.contrib import admin

from .models import Reservation, Employee

admin.site.register(Reservation)




from django.utils.html import format_html
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'profile_picture_tag')
    
	
    def profile_picture_tag(self, obj):
        if obj.profile_picture:
            return format_html(f'<img src="{obj.profile_picture.url}" style="width: 50px; height: 50px;" />')
        return "No Image"

    profile_picture_tag.short_description = "Profile Picture"
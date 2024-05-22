from django.contrib import admin




from.models import(
    ContactMessage,


)



class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'email',
        'phone',
        'created',
    ]

# Register your models here.

admin.site.register(ContactMessage, MessageAdmin)
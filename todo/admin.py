from django.contrib import admin
from.models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):#this is done to show up or readonly the hidden value named created which has been restricted by admin
    readonly_fields = ('created',)

admin.site.register(Todo,TodoAdmin)
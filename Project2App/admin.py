from django.contrib import admin
from .models import NewUserModel, RelatedContentModel, WikiModel


# Register your models here.

class WikiAdmin(admin.ModelAdmin):
    readonly_fields = ("date_made", "last_update")


admin.site.register(NewUserModel)
admin.site.register(RelatedContentModel)
admin.site.register(WikiModel)

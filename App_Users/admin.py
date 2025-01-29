from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users,Comments


class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ("email", "first_name", "last_name", "is_staff", "is_active")
    # list_filter = ("is_staff", "is_active", "groups")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "phone", "position", "nationalty", "image")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )


admin.site.register(Users, CustomUserAdmin)



class CommentsAdmin(admin.ModelAdmin):
    list_display = ("subject", "owner", "is_comment", "is_summary", "created")
    list_filter = ("is_comment", "is_summary", "created")
    search_fields = ("subject", "body", "owner__email")
    ordering = ("-created",)
    readonly_fields = ("created",)

    # Owner maydonini tanlashni majburiy qilish
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["owner"].required = True
        return form

admin.site.register(Comments, CommentsAdmin)
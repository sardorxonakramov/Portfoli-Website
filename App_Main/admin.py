from django.contrib import admin
from .models import (
    MyPersonal,
    Skill,
    Education,
    Experience,
    ExperienceDescription,
    Portfolio,
    Service
)


# MyPersonal modelini admin interfeysida sozlash
@admin.register(MyPersonal)
class MyPersonalAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "birth", "phone_number")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("degree",)
    ordering = ("first_name",)


# Skill modelini admin interfeysida sozlash
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "degree", "owner")
    search_fields = ("name", "owner__first_name")
    list_filter = ("degree",)


# Education modelini admin interfeysida sozlash
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "start_date", "finish_date")
    search_fields = ("name", "position")
    list_filter = ("start_date", "finish_date")


# Experience modelini admin interfeysida sozlash
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "start_date", "finish_date")
    search_fields = ("name", "position")
    list_filter = ("start_date", "finish_date")


# ExperienceDescription modelini admin interfeysida sozlash
@admin.register(ExperienceDescription)
class ExperienceDescriptionAdmin(admin.ModelAdmin):
    list_display = ("experience_id", "description")
    search_fields = ("experience_id__name",)
    list_filter = ("experience_id",)


# Portfolio modelini admin interfeysida sozlash
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name", "client", "project_date_finish", "project_url")
    search_fields = ("name", "client")
    list_filter = ("project_date_finish",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields= ('name',)
    list_filter = ('name',)
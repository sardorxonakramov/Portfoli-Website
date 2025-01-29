from modeltranslation.translator import register, TranslationOptions
from .models import (
    MyPersonal,
    Education,
    Experience,
    ExperienceDescription,
    Portfolio,
    Service,
)


@register(MyPersonal)
class MyPersonalTranslationOptions(TranslationOptions):
    fields = (
        "occupation",
        "personal_description",
        "job_description",
        "summary_description",
    )


@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ("position", "description",)



@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ("position",)



@register(ExperienceDescription)
class ExperienceDescriptionTranslationOptions(TranslationOptions):
    fields = ("description",)



@register(Portfolio)
class PortfolioTranslationOptions(TranslationOptions):
    fields = ("bio", "description",)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ("name", "description")
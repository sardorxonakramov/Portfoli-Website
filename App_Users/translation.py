from modeltranslation.translator import register, TranslationOptions
from .models import Users,Comments

@register(Users)
class UsersTranslationOptions(TranslationOptions):
    fields = ('position', 'nationalty')


@register(Comments)
class CommentsTranslationOptions(TranslationOptions):
    fields = ('subject', 'body')
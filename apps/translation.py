from modeltranslation.translator import register, TranslationOptions
from apps.models import Position, Branch, Shift


@register(Position)
class PositionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Branch)
class BranchTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Shift)
class ShiftTranslationOptions(TranslationOptions):
    fields = ('name',)

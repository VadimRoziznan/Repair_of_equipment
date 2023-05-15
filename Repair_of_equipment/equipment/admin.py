from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from equipment.models import Machine, GeneralTable


class GeneralTableInlineFormset(BaseInlineFormSet):
    def clean(self):
        tag_name = []
        is_main_count = 0
        for form in self.forms:
            pass
            # if form.cleaned_data.get('tag') in tag_name and form.cleaned_data.get('tag') is not None:
            #     raise ValidationError('Имена тегов не должны повторяться.')
            # else:
            #     tag_name.append(form.cleaned_data.get('tag'))
            # if form.cleaned_data.get('is_main'):
            #     is_main_count += 1
            # if is_main_count == 2:
            #     raise ValidationError('Количество избранных тегов не должно быть больше одного.')
        return super().clean()


class GeneralTableInline(admin.TabularInline):
    model = GeneralTable
    formset = GeneralTableInlineFormset
    extra = 0


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    inlines = [GeneralTableInline]





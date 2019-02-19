from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']
    list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date', 'question_type']


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)

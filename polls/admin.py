from django.contrib import admin
from .models import Question, Answer

# Register your models here.
class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1

class QuestionAdm(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = [
        (None, 
            {'fields': ['title', 'is_active']}
        ),
        ('Информация о дате',
            {'fields': ['date_published'], 
            'classes': ['collapse']}
        ),
    ]
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdm)

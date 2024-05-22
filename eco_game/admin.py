from django.contrib import admin
from .models import Question, Answer, Student, Result


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('q_id', 'q_text')


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('a_id', 'q_id', 'a_text', 'is_correct')
    list_filter = ('q_id', 'is_correct')
    search_fields = ('a_text',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('r_id', 'passed_at', 'student_id')
    search_fields = ('student_id__name',)
    list_filter = ('passed_at',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Result, ResultAdmin)

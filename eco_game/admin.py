from django.contrib import admin
from .models import Question, Answer, Student, Result

admin.site.register(Question)
admin.site.register(Answer)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('s_id', 'name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)


admin.site.register(Student, StudentAdmin)


class ResultAdmin(admin.ModelAdmin):
    list_display = ('r_id', 'passed_at', 'student_id')
    search_fields = ('student_id__name',)
    list_filter = ('passed_at',)


admin.site.register(Result, ResultAdmin)

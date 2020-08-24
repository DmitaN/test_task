from django.contrib import admin
from .models import Survey, Question, TypeQuestion, Answer, ResultSurvey

class SurveyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'dateBegin',
        'dateEnd',
        'description'
    )

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'surveyId',
        'title',
        'text',
        'type'
    )
    list_filter = ('surveyId',)

class TypeQuestionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )

class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'questionId ',
        'text',
    )
    list_filter = ('text',)

class ResultSurveyAdmin(admin.ModelAdmin):
    list_display = (
        'surveyId',
        'questionId',
        'answerId',
        'userId'
    )
    list_filter = ('UserId',)

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(TypeQuestion, TypeQuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(ResultSurvey, ResultSurveyAdmin)
# Register your models here.

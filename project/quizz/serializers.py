from rest_framework import serializers
from .models import Survey, Question, TypeQuestion, Answer, ResultSurvey
import datetime

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['pk', 'title', 'dateBegin', 'dateEnd', 'description', ]

    def get_active_survey(self):
        active_survey = Survey.objects.filter(dateEnd<datetime.datetime.now()).count()
        return active_survey



# Create your views here.

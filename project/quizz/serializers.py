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


class ResultSurvey(serializers.Serializer):
    results = serializers.JSONField()

    def validate_results(self, results):
        if not results:
            raise serializers.Validationerror("Results must be not null.")
        return results

    def save(self):
        results = self.data['results']
        user = self.context.userId
        for question_id in results:
            question = Question.objects.get(pk=question_id)
            choices = results[question_id]
            for answer_id in choices:
                choice = Choice.objects.get(pk=answer_id)
                ResultSurvey(userId=user, question=question, choice=choice).save()
                user.is_answer = True
                user.save()
# Create your views here.

from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=200)
    dateBegin = models.DateTimeField(editable=False)
    dateEnd = models.DateTimeField(editable=True)
    description = models.CharField(max_length=4096)

class Question(model.Model):
    surveyId = models.ForeignKey(TypeQuestion, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=4096)
    type = models.ForeignKey(TypeQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class TypeQuestion(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Answer(models.Model):
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=4096)

class ResultSurvey(models.Model):
    surveyId = models.ForeignKey(Survey, on_delete=models.CASCADE)
    questionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    answerId = models.ForeignKey(Answer, on_delete=models.CASCADE)
    userId = models.IntegerField()


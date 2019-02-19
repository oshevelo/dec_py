from django.db import models
from random import randint


class Question(models.Model):

    class QuestionType:
        easy='easy'
        hard='hard'
        medium='medium'

    QUESTION_TYPE_CHOICES = (
        (QuestionType.easy, "Very easy"),
        (QuestionType.hard, "Hard"),
        (QuestionType.medium, "Medium"),
    )

    question_text = models.CharField(max_length=200)
    question_description = models.TextField(default='')

    question_type = models.CharField(
        max_length=200,  
        choices=QUESTION_TYPE_CHOICES,
        default=QuestionType.easy
    )

    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    @property
    def was_published_recently(self):
        return bool(randint(0, 1))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


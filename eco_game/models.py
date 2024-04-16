from django.db import models


class Question(models.Model):
    q_id = models.AutoField(primary_key=True)
    q_text = models.TextField()

    def __str__(self):
        return self.q_text


class Answer(models.Model):
    a_id = models.AutoField(primary_key=True)
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    a_text = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.a_text

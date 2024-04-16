from django.db import models
from django.utils import timezone


class Question(models.Model):
    q_id = models.AutoField(primary_key=True, verbose_name="id")
    q_text = models.TextField(verbose_name="Вопрос")

    def __str__(self):
        return self.q_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    a_id = models.AutoField(primary_key=True, verbose_name="id")
    q_id = models.ForeignKey(Question, on_delete=models.CASCADE,
                             verbose_name="Вопрос")
    a_text = models.TextField(verbose_name="Ответ")
    is_correct = models.BooleanField(verbose_name="Правильный")

    def __str__(self):
        return self.a_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Student(models.Model):
    s_id = models.AutoField(primary_key=True, verbose_name="id")
    name = models.CharField(max_length=120, verbose_name="Имя")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    created_at = models.DateTimeField(default=timezone.now, editable=False,
                                      verbose_name="Дата регистрации")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Result(models.Model):
    r_id = models.AutoField(primary_key=True, verbose_name="id")
    passed_at = models.DateTimeField(default=timezone.now, editable=False,
                                     verbose_name="Дата прохождения")
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE,
                                   verbose_name="id студента")

    def __str__(self) -> str:
        return f"{self.passed_at.strftime('%Y-%m-%d %H:%M')}_{self.student_id.name}"

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'

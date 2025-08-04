import uuid
from django.db import models

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    INPUT_TYPES = (
        ('select', 'Seçmeli (Dropdown)'),
        ('text', 'Serbest Metin (Input)'),
    )

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    input_type = models.CharField(max_length=10, choices=INPUT_TYPES, default='select')

    def __str__(self):
        return f"{self.location.name} - {self.text}"

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.question.text} → {self.text}"


class Feedback(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    sent = models.BooleanField(default=False)
    responses = models.JSONField()

from django.db import models
from django.contrib.auth.models import User

class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    text = models.TextField()
    result = models.JSONField()  # Сохраняем ответ API нейросети
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Анализ {self.document.name} от {self.created_at}"

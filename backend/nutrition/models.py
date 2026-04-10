from django.db import models


class DietPlan(models.Model):
    title = models.CharField(max_length=150, unique=True)
    focus_area = models.CharField(max_length=120)
    breakfast = models.TextField()
    mid_morning = models.TextField()
    lunch = models.TextField()
    evening_snack = models.TextField()
    dinner = models.TextField()
    hydration_tip = models.TextField()
    lifestyle_tip = models.TextField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

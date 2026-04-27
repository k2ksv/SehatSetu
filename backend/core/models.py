from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Review(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    rating_overall = models.IntegerField()
    cleanliness = models.IntegerField()
    waiting_time = models.IntegerField()
    cost_transparency = models.IntegerField()
    facilities = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review {self.rating_overall}"


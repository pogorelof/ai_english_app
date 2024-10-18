from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=255)
    translation_to_ru = models.CharField(max_length=255, default="None")
    # Count of success translate
    guessed = models.PositiveIntegerField(default=0)
    # Count of fail with translate
    wrong = models.PositiveIntegerField(default=0)
    # True, if word was learned
    archive = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True, db_index=True)
    
    def __str__(self):
        return self.word
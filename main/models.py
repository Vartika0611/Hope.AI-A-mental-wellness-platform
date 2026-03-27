from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models
from django.utils import timezone

#questionnaire

class Assessment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='assessment_icons/', null=True, blank=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()

    def __str__(self):
        return self.text
#depression_test
 

class DepressionTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # <-- allow anonymous
    score = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Anonymous'} - Score: {self.score}"



# anxiety test
class AnxietyQuestion(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

#OCD test
from django.db import models
from django.utils import timezone

class OCDTestResult(models.Model):
    score = models.IntegerField()
    level = models.CharField(max_length=50)
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"OCD Score: {self.score} ({self.level}) at {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
#sleep_test


class SleepTestResult(models.Model):
    score = models.IntegerField()
    result_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sleep Score: {self.score} ({self.result_description})"
#self_esteem_test

class SelfEsteemTestResult(models.Model):
    score = models.IntegerField()
    level = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
#ptsd


class PTSDTestResult(models.Model):
    timestamp = models.DateTimeField(default=timezone.now)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()
    total_score = models.IntegerField()

    def __str__(self):
        return f"PTSD Test Result - {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} (Score: {self.total_score})"


#panel logic

from django.utils.text import slugify

class PanelMember(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.URLField()
    specialties = models.TextField(help_text="Comma-separated list")
    languages = models.TextField(help_text="Comma-separated list")
    description = models.TextField()
    slug = models.SlugField(blank=True, null=True)  # <- add this if not already there

    def get_specialties_list(self):
        return [s.strip() for s in self.specialties.split(",")]

    def get_languages_list(self):
        return [l.strip() for l in self.languages.split(",")]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            count = 1
            while PanelMember.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name



class Video(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    file = models.FileField(upload_to='videos/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.title



class Music(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    file = models.FileField(upload_to='music/')
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title




class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class EmotionReport(models.Model):
    user_name = models.CharField(max_length=100)
    stress = models.IntegerField()
    focus = models.IntegerField()
    mood = models.IntegerField()
    fatigue = models.IntegerField()
    calmness = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user_name




from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(default='', null=False)

    def __str__(self):
        return f"{self.name}"


class BrainBytes(models.Model):
    video = models.FileField(upload_to="videos/brain-bytes/", validators=[FileExtensionValidator(allowed_extensions=["mp4", "avif"])], blank=False, null=False)
    description = models.TextField()
    hashtags = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class CommentsB(models.Model):
    video = models.ForeignKey(BrainBytes, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Research(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="files/community/", validators=[FileExtensionValidator(allowed_extensions=["pdf", "txt"])], blank=True, null=True)
    public = models.BooleanField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class Cooperation(models.Model):
    title = models.CharField(max_length=255)
    people_quantity = models.PositiveIntegerField(default=1)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    searching_people = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class CommentsC(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    


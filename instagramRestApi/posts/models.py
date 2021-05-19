from django.db import models

"""
    user table: id(githubId)

    post table: id, caption, created_at, likes, userWhoLiked, imageUri, userId(foreign key)
"""

class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=32)

    def __repr__(self):
        return f"{self.id}: {self.name}"
    __str__ = __repr__

class Post(models.Model):
    currentName = models.CharField(max_length=32)
    caption = models.CharField(max_length=200, blank=True)
    avatarUrl = models.CharField(max_length=100)
    likes = models.ManyToManyField(User, related_name='liked', blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    imageType = models.CharField(max_length=50)
    imageBinary = models.BinaryField(editable=True, blank=False, null=False)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)

    def __repr__(self):
        return f"Post({self.id})"
    def total_likes(self):
        return self.likes.count()
    __str__ = __repr__
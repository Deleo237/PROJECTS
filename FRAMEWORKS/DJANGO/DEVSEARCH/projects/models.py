from django.db import models
from users.models import Profile
import uuid

# Create your models here.


# This is a table called Project
class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(
        null=True, blank=True
    )  # null is to allow or permit an empty record into the database while blank informs django that it can accept a record which is empty
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.URLField(max_length=2000, null=True, blank=True)
    source_link = models.URLField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )

    def __str__(self):
        return self.title


# This is a table called Review
class Review(models.Model):
    VOTE = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )

    def __str__(self):
        return self.value


# This is a table called Tag
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, db_index=True, editable=False
    )

    def __str__(self):
        return self.name

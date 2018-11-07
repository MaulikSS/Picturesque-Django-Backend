from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models, IntegrityError
from django.contrib.auth.models import User


# Create your models here.


# Creating a custom path for storing the user photos
# Example : /MEDIA_ROOT/photos/1234567890/abc.jpg
def path(instance, filename):
    return 'photos/{0}/{1}'.format(instance.author.username, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, null=True)
    display = models.FileField(blank=True, null=True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_written')
    caption = models.TextField(max_length=500)
    photo = models.FileField(upload_to=path)
    likes = models.ManyToManyField(User, related_name='posts_liked', blank=True)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.author.username + " - " + str(self.time)


'''
    def save(self, *args, **kwargs):
    if not self.id:
        self.time = timezone.now()
    return super(Post, self).save(*args, **kwargs)
'''


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.author.username + " - " + self.post.id + " - " + self.time


'''
    def save(self, *args, **kwargs):
        if not self.id:
            self.time = timezone.now()
        return super(Comment, self).save(*args, **kwargs)
'''

'''
class FollowRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = 'request_sent')
    receiver = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = 'request_received')
    created_on = models.DateTimeField(default=datetime.now)
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username + " -> " + self.receiver.username

    @classmethod
    def create_request(cls, sender, receiver):
        follow_request, created = FollowRequest.objects.get_or_create(sender=sender, receiver=receiver, accepted=False, rejected=False)

    def accept(self):
        self.accepted = True

    def reject(self):
        self.rejected = True


class RelationshipManager(models.Manager):

    def get_all_followers(self, user):
        try:
            followers = Relationship.objects.filter(following=user).all()
        except Relationship.DoesNotExist:
            followers = []
        return followers

    def get_all_followings(self, user):
        try:
            followings = Relationship.objects.filter(follower=user).all()
        except Relationship.DoesNotExist:
            followings = []
        return followings

    def add_relationship(self, follower, following):
        if follower == following:
            raise ValidationError("Users cannot follow themselves")

        relationship, created = Relationship.objects.get_or_create(follower=follower, following=following)

        if created is False:
            raise IntegrityError("Relationship Already Exists")

        return relationship

    def remove_relation(self, pk):
        try:
            relationship = Relationship.objects.get(pk=pk)
            relationship.delete()
            return True
        except Relationship.DoesNotExist:
            return False

class Relationship(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_relationship')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_relationship')
    created_on = models.DateTimeField(default=datetime.now)

    objects = RelationshipManager()

    def __str__(self):
        return self.follower.username + " -> " + self.following.username

    def save(self, *args, **kwargs):
        if self.follower == self.following:
            raise ValidationError("Users cannot follow themselves")
        super(Relationship, self).save(*args, **kwargs)
        
'''

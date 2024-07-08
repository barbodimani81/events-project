from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Event(models.Model):
    """
    A class to create events in the app.
    """
    title = models.CharField(max_length=255)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    A class to create the categories for events.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('id',)

    def __str__(self):
        return self.title


class Session(models.Model):
    """
    A class to create sessions for an event.
    """
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'
        ordering = ('id',)

    def __str__(self):
        return self.title

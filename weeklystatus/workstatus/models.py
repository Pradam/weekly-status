from django.db import models

# Create your models here.

ACTIVE = ((0, 0), (2, 2))

STATUS = ((0, 'This Week'), (2, 'Next Week'))

OPTIONAL = {'null': True, 'blank': True}


class BaseContent(models.Model):
    createdOn = models.DateTimeField(auto_now_add=True)
    modifiedOn = models.DateTimeField(auto_now=True)
    active = models.IntegerField(choices=ACTIVE, default=2)

    class Meta:
        abstract = True


class WorkDescription(BaseContent):
    status = models.IntegerField(choices=STATUS, default=0)
    description = models.TextField()

    def __str__(self):
        return "%s" % self.get_status_display()
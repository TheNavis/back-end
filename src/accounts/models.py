from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Account(models.Model):
    user = models.OneToOneField(User, verbose_name=_('User'), related_name='investor', on_delete=models.CASCADE)
    phone = models.CharField(max_length=8)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        user = self.user
        return '%s %s' % (user.first_name, user.last_name)

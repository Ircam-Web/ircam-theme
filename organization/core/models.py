from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse, reverse_lazy
from mezzanine.pages.models import Page, RichText
from mezzanine.core.fields import RichTextField, OrderField, FileField
from django.conf import settings

from organization.media.models import Photos

ALIGNMENT_CHOICES = (('left', _('left')), ('right', _('right')))
MEDIA_BASE_URL = getattr(settings, 'MEDIA_BASE_URL', 'http://medias.ircam.fr/embed/media/')



class Named(models.Model):
    """Named object with description"""

    name = models.CharField(_('name'), max_length=512)
    description = models.TextField(_('description'), blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    @property
    def slug(self):
        return slugify(self.__unicode__())


class SubTitle(models.Model):

    sub_title = models.TextField(_('sub title'), blank=True, max_length=1024)

    class Meta:
        abstract = True


class BasicPage(Page, RichText, SubTitle, Photos):

    class Meta:
        verbose_name = 'basic page'
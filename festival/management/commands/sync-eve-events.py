from datetime import datetime, timedelta
from optparse import make_option

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

import mezzanine_agenda.models as ma_models
import eve.models as eve_models


class Command(BaseCommand):
    """Synchronize events from E-vement to mezzanine_agenda"""


    option_list = BaseCommand.option_list + (
          make_option('-m', '--meta_event',
            dest='meta_event',
            help='define eve meta_event'),
          )

    default_user = User.objects.get(username='admin')

    def cleanup(self):
        for event in ma_models.Event.objects.all():
            event.delete()
        for location in ma_models.EventLocation.objects.all():
            location.delete()

    def handle(self, *args, **kwargs):
        self.cleanup()
        meta_event_name = kwargs.get('meta_event')
        meta_trans_all = eve_models.MetaEventTranslation.objects.all()
        for meta_trans in meta_trans_all:
            if meta_trans.name == meta_event_name:
                break
        eve_events = eve_models.Event.objects.filter(meta_event=meta_trans.id)
        for eve_event in eve_events:
            event_trans = eve_models.EventTranslation.objects.filter(id=eve_event, lang='fr')[0]
            manifestations = eve_event.manifestations.all().order_by('happens_at')
            first = True
            for manifestation in manifestations:
                events = ma_models.Event.objects.filter(external_id=manifestation.id)
                if not events:
                    event = ma_models.Event(external_id=manifestation.id)
                else:
                    event = events[0]
                event.start = manifestation.happens_at
                event.end = manifestation.happens_at + timedelta(seconds=manifestation.duration)
                event.title = event_trans.name
                event.user = self.default_user
                
                location, c = ma_models.EventLocation.objects.get_or_create(title=manifestation.location.name)
                address = '\n'.join([manifestation.location.address, manifestation.location.postalcode + ' ' + manifestation.location.city])
                location.address = address
                location.clean()
                location.save()
                event.location = location

                category, c = ma_models.EventCategory.objects.get_or_create(name=eve_event.event_category.name)
                event.category = category

                if not first:
                    event.parent = parent
                else:
                    parent = event
                    first = False

                event.save()

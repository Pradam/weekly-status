import datetime
from django.core.management.base import BaseCommand, CommandError
from workstatus import WorkDescription

class Durations(object):

    @classmethod
    def get_current_week_date(cls):
        today = datetime.datetime.now().date()
        dates = [today + datetime.timedelta(days=i) for i in \
                 range(0 - today.weekday(), 5 - today.weekday())]
        start_week = dates[0]
        end_week = dates[-1]
        return start_week, end_week


class Command(BaseCommand):
    help = 'Automating the weekly status'

    def handle(self, *args, **options):
        start, end = Durations.get_current_week_date()
        get_current_week_desc = WorkDescription.objects.filter(active=2, createdOn__gte=start, createdOn__lte=end)
        

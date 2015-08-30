import time
import pytz
import datetime
import calendar
import collections
from bisect import bisect_left

from dateutil.relativedelta import relativedelta
from django.db.models import QuerySet
from django.utils import timezone


# Useful functions.

ts_min = lambda ts: pytz.utc.localize(
        datetime.datetime.combine(ts, datetime.time.min))
ts_max = lambda ts: pytz.utc.localize(
        datetime.datetime.combine(ts, datetime.time.max))

def MonthBoundary(year, month):
    """
        Returns the first and the last datatime.datetime
        from a given month.
    """
    y, m = int(year), int(month)
    days = calendar.monthrange(y, m)

    first = datetime.date(year=y, month=m, day=1)
    last = datetime.date(year=y, month=m, day=days[-1])

    month_boundaries = collections.namedtuple('MonthBoundary',
            ['first', 'last'])

    # Ugly gambi
    try:
        return month_boundaries(pytz.utc.localize(ts_min(first)),
                                pytz.utc.localize(ts_max(last)))
    except ValueError:
        return month_boundaries(ts_min(first), ts_max(last))


def each_last_reading(readings, first, last, delta):
    """
        Returns the last reading of each period in range.
        - Range is representd by first and last
        - Period is representd by delta

        * This functions uses the bisection algorithm,
        so `readings` must be sorted!
        * Each object in `readings` must support __lt__
        * Only on Python 3.6 bisect will support key=
    """

    list(readings).sort(key=lambda x: x.timestamp)
    closing_dict = collections.OrderedDict()
    current = first

    while True:
        # Get the first value before current
        index = bisect_left(readings, current)
        if index:
            closing_dict[index-1] = readings[index-1]
        print(last, current)
        if current > last:
            break
        current += delta

    return closing_dict.values()

class TimeseriesQuerySet(QuerySet):

    def year(self, timestamp):
        year = timestamp.year

        jan_1st = ts_min(datetime.datetime(year, 1, 1))
        dec_31st = ts_max(datetime.datetime(year, 12, 31))

        return self.filter(
            timestamp__range=(
                jan_1st, dec_31st)).order_by('timestamp')

    def month(self, timestamp):
        year, month = timestamp.year, timestamp.month
        mb = MonthBoundary(year, month)
        return self.filter(
                timestamp__range=(
                    mb.first, mb.last)).order_by('timestamp')

    def day(self, timestamp):
        return self.filter(
                timestamp__range=(
                    ts_min(timestamp),
                    ts_max(timestamp)
                )
            ).order_by('timestamp')

    property
    def daily_closing(self):
        delta = relativedelta(days=+1)
        first = ts_min(self.earliest('timestamp').timestamp)
        last = ts_max(self.latest('timestamp').timestamp)
        return each_last_reading(self, first, last, delta)

    @property
    def monthly_closing(self):
        first = ts_min(self.earliest('timestamp').timestamp)
        mb = MonthBoundary(first.year, first.month)
        last = ts_max(self.latest('timestamp').timestamp)
        delta = relativedelta(months=+1)
        return each_last_reading(self, mb.first, last, delta)

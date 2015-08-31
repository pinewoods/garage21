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


def each_last_reading(readings, first, last, delta, ts_field):
    """
        Returns the last reading of each period in range.
        - Range is representd by first and last
        - Period is representd by delta

        * This functions uses the bisection algorithm,
        so `readings` must be sorted!
        * Each object in `readings` must support __lt__
        * Only on Python 3.6 bisect will support key=
    """

    list(readings).sort(key=lambda x: getattr(x, ts_field))
    closing_dict = collections.OrderedDict()
    current = first

    while True:
        # Get the first value before current
        index = bisect_left(readings, current)
        if index:
            closing_dict[index-1] = readings[index-1]

        if current > last:
            break
        current += delta

    return closing_dict.values()


class TimeseriesQuerySet(QuerySet):

    @property
    def _ts_field(self):
        return self.model.Extra.ts_field

    def year(self, timestamp):
        year = timestamp.year

        jan_1st = ts_min(datetime.datetime(year, 1, 1))
        dec_31st = ts_max(datetime.datetime(year, 12, 31))

        kwargs = {'%s__range' % self._ts_field: (jan_1st, dec_31st)}
        return self.filter(**kwargs).order_by(self._ts_field)

    def month(self, timestamp):
        year, month = timestamp.year, timestamp.month
        mb = MonthBoundary(year, month)
        kwargs = {'%s__range' % self._ts_field: (mb.first, mb.last)}
        return self.filter(**kwargs).order_by(self._ts_field)

    def day(self, timestamp):
        kwargs = {'%s__range' % self._ts_field:
                (ts_min(timestamp), ts_max(timestamp))}
        return self.filter(**kwargs).order_by(self._ts_field)

    @property
    def daily_closing(self):
        delta = relativedelta(days=+1)
        get_ts = lambda x: getattr(x, self._ts_field)
        first = ts_min(get_ts(self.earliest(self._ts_field)))
        last = ts_max(get_ts(self.latest(self._ts_field)))
        return each_last_reading(self, first, last, delta, self._ts_field)

    @property
    def monthly_closing(self):
        get_ts = lambda x: getattr(x, self._ts_field)
        first = ts_min(get_ts(self.earliest(self._ts_field)))
        last = ts_max(get_ts(self.latest(self._ts_field)))
        mb = MonthBoundary(first.year, first.month)
        delta = relativedelta(months=+1)
        return each_last_reading(self, mb.first, last, delta, self._ts_field)

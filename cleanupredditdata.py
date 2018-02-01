from datetime import datetime
from dateutil import tz

################ CLEAN UP TIME ######################
# METHOD 1: Hardcode zones:
from_zone = tz.gettz('UTC')
to_zone = tz.gettz('America/New_York')

# METHOD 2: Auto-detect zones:
from_zone = tz.tzutc()
to_zone = tz.tzlocal()

# utc = datetime.utcnow()
utc = datetime.strptime('2011-01-21 02:37:21', '%Y-%m-%d %H:%M:%S')

# Tell the datetime object that it's in UTC time zone since
# datetime objects are 'naive' by default
utc = utc.replace(tzinfo=from_zone)

# Convert time zone
central = utc.astimezone(to_zone)

################ CLEAN UP TIME ######################
import time

# UTC TO LOCAL different method
def datetime_from_utc_to_local(utc_datetime):
    now_timestamp = time.time()
    offset = datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)
    return utc_datetime + offset

################ CLEAN UP TIME ######################
from datetime import datetime,tzinfo,timedelta

class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
            return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
         return self.name

GMT = Zone(0,False,'GMT')
EST = Zone(-5,False,'EST')

print datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S %Z')
print datetime.now(GMT).strftime('%m/%d/%Y %H:%M:%S %Z')
print datetime.now(EST).strftime('%m/%d/%Y %H:%M:%S %Z')

t = datetime.strptime('2011-01-21 02:37:21','%Y-%m-%d %H:%M:%S')
t = t.replace(tzinfo=GMT)
print t
print t.astimezone(EST)
import datetime


class TimeUtils(object):
    def __init__(self, datetime=datetime.datetime.now()):
        self.datetime = datetime

    def get_minutes(self):
        splitted_time = str(self.datetime).split(" ")
        splitted_hours = splitted_time[1].split(":")
        minute_timestamp = splitted_time[0]+"T" + \
            splitted_hours[0]+":"+splitted_hours[1]+":00.000"

        return minute_timestamp

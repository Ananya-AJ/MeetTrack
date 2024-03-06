from datetime import datetime

def get_unixtime(hour=0, minute=0, second=0, millisecond=0):
    timestamp = datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute, second, millisecond*1000)
    unixtime = timestamp.timestamp()
    return unixtime
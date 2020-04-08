from datetime import datetime

timezone = 'PST'

def process_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('')

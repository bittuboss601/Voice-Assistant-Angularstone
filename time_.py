def time_():
    response = ''
    now = datetime.datetime.now()
    meridiem = ''
    if now.hour >=12:
        meridiem = 'p.m'
        hour = now.hour -12
    else:
        meridiem = 'a.m'
        hour = now.hour
    # convert minute into a proper string
    if now.minute < 10:
        minute = '0' + str(now.minute)
    else:
        minute = str(now.minute)
        response = response + ' ' + 'It is ' + str(hour) + ':' + minute + ' ' + meridiem + '.'
        return response
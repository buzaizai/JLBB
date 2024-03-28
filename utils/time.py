from datetime import datetime,timedelta
import pytz

# UTC+8 timezone name
timezone_name = 'Asia/Shanghai'

'''
precision scales for @getNowTime
'''
precisions={
    'second': '%Y-%m-%d %H:%M:%S',
    'minute': '%Y-%m-%d %H:%M',
    'hour': '%Y-%m-%d %H',
    'day': '%Y-%m-%d'
}


def getNowTime(toStr=False, precision='second'):
    ''' Get now time with timezone, default: UTC+8, default precision: second
    
    :param toStr: return str or datetime, default: False (return datetime)
    :param precision: return time with precision, default: 'second', optional: 'minute', 'hour', 'day'
    '''
    utc_now = datetime.utcnow()
    timezoneCN = pytz.timezone(timezone_name)
    local_now = utc_now.replace(tzinfo=pytz.timezone('UTC')).astimezone(timezoneCN)
    
    try:
        if precision == 'second':
            local_now = local_now.replace(microsecond=0)
        elif precision == 'minute':
            local_now = local_now.replace(second=0, microsecond=0)
        elif precision == 'hour':
            local_now = local_now.replace(minute=0, second=0, microsecond=0)
        elif precision == 'day':
            local_now = local_now.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            # Invalid precision, use default precision 'second'
            local_now = local_now.replace(microsecond=0)
            raise Exception(f"precision '{precision}' is not defined")

        if toStr:
                _precision=precisions[precision]
                if _precision:
                    local_now = local_now.strftime(_precision)
                else:
                    raise Exception(f"precision '{precision}' is not defined")
    except Exception as e:
                print(f"getNowTime: {e}, use default precision 'second'")
    finally:
        return local_now


def getNowTimeWithOffset(days=0,hours=0):
    ''' Get now time with offset(days,hours), precision: minute

    :param days: offset days, default: 0
    :param hours: offset hours, default: 0
    :return: now time (datetime) with offset
    '''
    timeNow = getNowTime(precision='minute')
    if days != 0:
        timeNow += timedelta(days=days)
    if hours != 0:
        timeNow += timedelta(hours=hours)
    return timeNow
    
if __name__ == '__main__':
    pass

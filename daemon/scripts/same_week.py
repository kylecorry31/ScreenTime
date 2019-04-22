import datetime
import sys

def get_year(m_time):
    return datetime.datetime.fromtimestamp(m_time).year


def get_week_number(m_time):
    return datetime.datetime.fromtimestamp(m_time).isocalendar()[1]

def on_same_week(time1, time2):
    return get_year(time1) == get_year(time2) and get_week_number(time1) == get_week_number(time2)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(on_same_week(int(sys.argv[1]), int(sys.argv[2])))
